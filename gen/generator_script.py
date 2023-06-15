"""
Script to re-generate the ``apteco-api`` package
based on the API spec at the given source.

This only generates the Python source code;
it does *not* then build a distribution from it or publish it to PyPI.

Calling routines (all have optional -p):

    1) Fetch spec from API instance: -u
    2) Fetch spec from file with version no. in filename: -f
    3) Fetch spec from file and supply version no.: -fs
    4) Supply new version no. (e.g. having manually changed spec): -s
    5) Just bump package version (without changing spec): -p

"""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

import parse
import semver
from urlpath import URL

API_SPEC_PATH = "gen/api-spec.json"
INTRODUCTION_PATH = "introduction.md"
GEN_CONFIG_PATH = "gen/config.yaml"
GEN_VERSION = "4.3.1"
README_PATH = "README.md"
VERSION_PARTS = ["major", "minor", "patch", "dev_num"]


def parse_options():
    """Parse command line options passed to script."""
    parser = argparse.ArgumentParser()
    source_group = parser.add_mutually_exclusive_group()
    source_group.add_argument("-u", "--url", type=str, help="URL of OrbitAPI to retrieve spec from")
    source_group.add_argument("-f", "--file", type=Path, help="filepath of OrbitAPI spec to use")
    parser.add_argument("-s", "--spec-version", type=str, help="OrbitAPI spec version")
    parser.add_argument("-p", "--part", type=str, choices=VERSION_PARTS, help="version part to increase when bumping package version")

    args = parser.parse_args()
    if not any(vars(args).values()):  # print help if no arguments passed
        parser.parse_args(["-h"])
    if args.url and args.spec_version:
        parser.error("argument -s/--spec-version: not allowed with argument -u/--url")
    if args.part is None:
        args.part = "minor"

    return args


def fetch_orbit_spec_version_no(api_base_url):
    """Get the Orbit API spec version number from the given source."""
    spec_version_url = URL(api_base_url) / "About/Version"
    spec_version_response = spec_version_url.get()
    spec_version = spec_version_response.json().get("version")
    if spec_version is None:
        raise LookupError("Failed to fetch OrbitAPI spec version number.")
    else:
        return spec_version


def get_spec_from_api(api_base_url):
    """Get the spec and version at the given source."""
    spec_url = URL(api_base_url) / "swagger/v2/swagger.json"
    spec_response = spec_url.get()
    spec = spec_response.json()

    version = fetch_orbit_spec_version_no(api_base_url)

    return spec, version


def get_spec_from_file(spec_source, version=None):
    """Load the spec from the given file."""
    spec_source_path = Path(spec_source)
    with open(spec_source_path) as f:
        spec = json.load(f)

    if version is None:
        match = re.match(r"OrbitAPI-spec-([0-9.]+)(-formatted)?", spec_source_path.stem)
        if match is None:
            raise ValueError(
                "No version number was provided"
                " and it could not be derived from spec source filename."
            )
        version = match[1]

    return spec, version


def update_spec(spec, api_spec_path=API_SPEC_PATH):
    """Update the API Swagger spec using the one provided."""
    spec.update({"host": "example.com", "basePath": "/OrbitAPI/"})
    fix_spec_issues(spec)
    api_spec_path = Path(api_spec_path)
    with open(api_spec_path, "w") as f:
        f.write(json.dumps(spec, indent=4, ensure_ascii=False))


def fix_spec_issues(spec):
    """Apply manual fixes to spec."""

    # lastLogin property in SessionDetails should be optional
    session_details_required = spec["definitions"]["SessionDetails"]["required"]
    if "lastLogin" in session_details_required:
        session_details_required.remove("lastLogin")
    else:
        print("Spec issue not detected: `lastLogin` property for `SessionDetails` already set as optional")


def find_line_no(content_lines, match_text, error_message):
    """Find line number where given content occurs."""
    for line_no, line in enumerate(content_lines):
        if line.startswith(match_text):
            return line_no
    else:
        raise LookupError(error_message)


def update_orbit_spec_version_number(orbit_version, introduction_path=INTRODUCTION_PATH, gen_version=GEN_VERSION):
    """Write new Orbit API spec version number into README content."""
    with open(introduction_path, "r") as f:
        introduction_content = f.readlines()

    spec_version_line_no = find_line_no(
        introduction_content,
        "- OrbitAPI spec version:",
        "Couldn't find where to change OrbitAPI spec version number in Introduction."
    )
    introduction_content[spec_version_line_no] = f"- OrbitAPI spec version: {orbit_version}\n"
    gen_version_line_no = find_line_no(
        introduction_content,
        "- Generator version:",
        "Couldn't find where to change Generator version number in Introduction."
    )
    introduction_content[gen_version_line_no] = f"- Generator version: {gen_version}\n"

    with open(introduction_path, "w") as f:
        f.writelines(introduction_content)


def fetch_and_update_spec(url=None, filepath=None, version=None):
    """Update the package with a new spec from the supplied source."""
    if url and filepath:
        raise ValueError("Can only specify one of url or filepath")

    new_spec, new_version = None, None
    if url:
        new_spec, new_version = get_spec_from_api(url)
    if filepath:
        new_spec, new_version = get_spec_from_file(filepath, version)

    if new_spec is not None:
        update_spec(new_spec)
        update_orbit_spec_version_number(new_version)
        return new_version
    elif version is not None:
        update_orbit_spec_version_number(version)
        return version


def get_new_version(output):
    """Parse new version number from version bumping output."""
    output = output.strip()
    out_lines = output.split("\r\n")
    (current,) = [line for line in out_lines if line.startswith("current_version")]
    (tag,) = [line for line in out_lines if line.startswith("tag")]
    (commit,) = [line for line in out_lines if line.startswith("commit")]
    (new,) = [line for line in out_lines if line.startswith("new_version")]
    try:
        current_text, current_version_no = current.split("=")
        new_text, new_version_no = new.split("=")
        assert tag == "tag=False"
        assert commit == "commit=False"
        assert current_text == "current_version"
        assert new_text == "new_version"
    except (AssertionError, ValueError) as exc:
        raise ChildProcessError(f"Unexpected output from bumping version:\n{output}") from exc

    if not semver.compare(new_version_no, current_version_no) > 0:
        raise ChildProcessError(
            "Version not bumped as expected:\n"
            f"Current version: {current_version_no}\n"
            f"New version: {new_version_no}\n"
            "(new version does not compare as greater than current)"
        )

    return new_version_no


def bump_package_version(part="minor", allow_dirty=False):
    """Bump version and return new version number if successful."""
    if part not in VERSION_PARTS:
        raise ValueError(f"'{part}' is not a valid part parameter.")
    allow_dirty_arg = ["--allow-dirty"] if allow_dirty else []
    args = ["bumpversion"] + allow_dirty_arg + ["--list", part]

    result = subprocess.run(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    if result.stderr:
        err_text = result.stderr.decode('utf-8')
        if err_text.startswith("Git working directory is not clean:"):
            raise ChildProcessError(f"Bumping version failed: Git working directory is not clean.")
        else:
            raise ChildProcessError(f"{err_text}\n Bumping version failed for unknown reason. (see error text above)")
    else:
        out_text = result.stdout.decode('utf-8').strip()

    return get_new_version(out_text)


def delete_old_package():
    """Remove code, docs and tests for existing package."""
    shutil.rmtree("apteco_api/")
    shutil.rmtree("docs/")
    shutil.rmtree("test/")


def generate_new_package(api_spec_path=API_SPEC_PATH, gen_config_path=GEN_CONFIG_PATH, gen_version=GEN_VERSION):
    """Run package generator process and return result."""
    args = [
        fr"java -jar gen\openapi-generator-cli-{gen_version}.jar generate",
        f"-i {api_spec_path}",
        "-g python",
        "-o .",
        f"-c {gen_config_path}",
    ]
    return subprocess.run(
        " ".join(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def check_generator_output(result):
    """Check for and return important info from package generator."""
    COMMON_WARNINGS = [
        "[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in content, returning only the first one",
        "[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/json)",
        "[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (application/json-patch+json)",
        "[main] WARN  o.o.codegen.utils.ModelUtils - Multiple schemas found in the OAS 'content' section, returning only the first one (text/xml)",
        "[main] WARN  o.o.c.languages.PythonClientCodegen - Property (reserved word) cannot be used as model name. Renamed to ModelProperty",
        "[main] WARN  o.o.codegen.DefaultCodegen - Multiple MediaTypes found, using only the first one",
    ]
    OTHER_WARNINGS = [
        "[main] WARN  o.o.c.languages.PythonClientCodegen - Type object not handled properly in setParameterExampleValue",
        "[main] WARN  o.o.c.languages.PythonClientCodegen - Type list not handled properly in setParameterExampleValue",
        "[main] INFO  o.o.codegen.DefaultGenerator - Model ReferenceVariableInfo not generated since it's a free-form object",
    ]
    STANDARD_INFO = [
        "[main] INFO  o.o.codegen.DefaultGenerator - Generating with dryRun=false",
        "[main] INFO  o.o.codegen.DefaultGenerator - OpenAPI Generator: python (client)",
        "[main] INFO  o.o.codegen.DefaultGenerator - Generator 'python' is considered stable.",
        "[main] INFO  o.o.c.languages.PythonClientCodegen - Environment variable PYTHON_POST_PROCESS_FILE not defined so the Python code may not be properly formatted. To define it, try 'export PYTHON_POST_PROCESS_FILE=\"/usr/local/bin/yapf -i\"' (Linux/Mac)",
        "[main] INFO  o.o.c.languages.PythonClientCodegen - NOTE: To enable file post-processing, 'enablePostProcessFile' must be set to `true` (--enable-post-process-file for CLI).",
    ]
    OKAY_TO_IGNORE = COMMON_WARNINGS + OTHER_WARNINGS + STANDARD_INFO
    GENERATOR_IGNORE_FORMAT = "[main] INFO  o.o.codegen.DefaultGenerator - Skipped generation of {base_path}\\.\\{file_path} due to rule in .openapi-generator-ignore"
    WRITE_INFO_MESSAGE_START = "[main] INFO  o.o.codegen.AbstractGenerator - writing file"

    outlines = result.stdout.decode("utf-8").strip().split("\r\n")
    significant = [line for line in outlines if not (line in OKAY_TO_IGNORE or line.startswith(WRITE_INFO_MESSAGE_START))]

    skips = []
    unrecognised = []
    for line in significant:
        result = parse.parse(GENERATOR_IGNORE_FORMAT, line)
        if result is not None:
            skips.append(result["file_path"])
        else:
            unrecognised.append(line)

    if unrecognised:
        message = "Running the generator produced the following unrecognised log messages:\n"
        message += "\n".join(unrecognised)
        raise ChildProcessError(message)

    if skips:
        message = "The following files were skipped based on the .openapi-generator-ignore rules:\n"
        message += "\n".join(skips)
    else:
        message = "No files were skipped based on the .openapi-generator-ignore rules."

    return message


def fix_generated_package_issues():
    """Apply manual fixes to generated package."""
    return fix_parameters_with_path_format_issue()


def fix_parameters_with_path_format_issue():
    """Fix issue with parameters whose format is 'path' not being handled correctly."""
    with open(API_SPEC_PATH) as f:
        spec = json.load(f)

    parameter_matches = []
    for path, operations in spec["paths"].items():
        for verb, operation in operations.items():
            for idx, parameter in enumerate(operation["parameters"]):
                if parameter.get("format") == "path":
                    parameter_matches.append({
                        "path": path,
                        "verb": verb,
                        "operation_id": operation["operationId"],
                        "param_idx": idx,  # not used
                        "param_name": parameter["name"],
                    })

    output_message = ""
    for match in parameter_matches:
        output_message += fix_path_format_parameter(
            match["path"],
            match["verb"],
            match["operation_id"],
            match["param_name"],
        )

    return output_message


def fix_path_format_parameter(path, verb, operation_id, param_name):
    """Insert code snippet to correctly handle parameter with 'path' format."""
    api, method = operation_id.split("_")

    api_split = re.split("(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", api)
    api_py = "_".join(api_split).lower()
    method_split = re.split("(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", method)
    method_name_py = "_".join(method_split).lower()
    param_name_split = re.split("(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", param_name)
    param_name_py = "_".join(param_name_split).lower()

    full_method_name_py = f"{api_py}_{method_name_py}"
    api_filename = f"apteco_api/api/{api_py}_api.py"
    var_name_prefix = param_name_py

    with open(api_filename) as f:
        code_lines = f.readlines()

    method_definitions = [(line_no, line) for line_no, line in enumerate(code_lines) if line.startswith("    def ")]
    ((method_idx, method_line_no),) = [(idx, line_no) for idx, (line_no, line) in enumerate(method_definitions) if line.startswith(f"    def {full_method_name_py}_with_http_info(")]
    try:
        next_method_line_no = method_definitions[method_idx + 1][0]
    except IndexError:  # this method is the last one
        next_method_line_no = len(code_lines)
    before_method, method_lines, after_method = code_lines[:method_line_no], code_lines[method_line_no:next_method_line_no], code_lines[next_method_line_no:]

    # check for cases where parameter name gets `_` prepended by the generator (presumably to avoid collision with reserved name)
    if f", {param_name_py}" not in method_lines[0]:
        if f", _{param_name_py}" in method_lines[0]:
            param_name_py = f"_{param_name_py}"
        else:
            raise ValueError(f"Parameter `{param_name_py}` not found in signature of method `{full_method_name_py}()`")

    param_section_find = f"""
        if '{param_name_py}' in local_var_params:
            path_params['{param_name}'] = local_var_params['{param_name_py}']  # noqa: E501"""
    param_section_replace = f"""
        if '{param_name_py}' in local_var_params:
            # handle '{param_name_py}' correctly as parameter with 'path' format 
            {var_name_prefix}_segments = local_var_params['{param_name_py}'].split('/')
            {var_name_prefix}_extra_path_params = {{f'{param_name}{{i}}': seg for i, seg in enumerate({var_name_prefix}_segments)}}
            {var_name_prefix}_template = '/'.join(f'{{{{{{k}}}}}}' for k in {var_name_prefix}_extra_path_params.keys())
            path_params.update({var_name_prefix}_extra_path_params)
        else:
            {var_name_prefix}_template = '{{{param_name}}}'"""

    path_before, __, path_after = path.partition(f"{{{param_name}}}")
    api_call_section_find = f"""return self.api_client.call_api(
            '{path}', '{verb.upper()}',"""
    api_call_section_replace = f"""return self.api_client.call_api(
            {f"'{path_before}' + " if path_before else ""}{var_name_prefix}_template{f" + '{path_after}'" if path_after else ""}, '{verb.upper()}',"""

    method_text = "".join(method_lines)
    assert method_text.count(param_section_find) == 1, f"Could not find check for parameter `{param_name_py}` in method `{method_name_py}()`"
    modified_method_text = method_text.replace(param_section_find, param_section_replace)
    assert modified_method_text.count(api_call_section_find) == 1, f"Could not find API client call with parameter `{param_name_py}` in method `{method_name_py}()`"
    modified_method_text = modified_method_text.replace(api_call_section_find, api_call_section_replace)
    modified_code = "".join(before_method) + modified_method_text + "".join(after_method)

    with open(api_filename, "w") as f:
        f.write(modified_code)

    return f"Applied fix for path-formatted parameter `{param_name}` in method `{api}Api.{method_name_py}()`\n"


def regenerate_package():
    """Delete old package, generate new version and check output."""
    delete_old_package()
    result = generate_new_package()
    generator_output = check_generator_output(result)
    generator_fixes_output = fix_generated_package_issues()
    return generator_output + "\n" + generator_fixes_output


def update_readme(readme_path=README_PATH, introduction_path=INTRODUCTION_PATH):
    """Update static README content with generated docs links."""
    with open(readme_path, "r") as f:
        readme_content = f.readlines()
    doc_start_line_no = find_line_no(
        readme_content,
        "## Documentation for API Endpoints",
        "Couldn't find start of documentation section in README."
    )
    doc_end_line_no = find_line_no(
        readme_content,
        "## Author",
        "Couldn't find end of documentation section in README."
    )

    with open(introduction_path, "r") as f:
        introduction_content = f.readlines()
    introduction_author_line_no = find_line_no(
        introduction_content,
        "## Author",
        "Couldn't find author section in Introduction."
    )

    with open(readme_path, "w") as f:
        f.writelines(
            introduction_content[:introduction_author_line_no]
            + readme_content[doc_start_line_no:doc_end_line_no]
            + introduction_content[introduction_author_line_no:]
        )


def convert_line_endings_to_lf(file_path):
    """Re-write the file with LF line endings."""
    with open(file_path, "r") as f:
        content = f.readlines()

    with open(file_path, "w", newline="\n") as f:
        f.writelines(content)


def correct_line_endings():
    """Convert files with CRLF line endings to LF."""
    for file_path in (
            API_SPEC_PATH,
            GEN_CONFIG_PATH,
            "setup.py",
            ".bumpversion.cfg",
            README_PATH,
    ):
        convert_line_endings_to_lf(file_path)


def main():
    args = parse_options()
    orbit_spec_version_number = fetch_and_update_spec(args.url, args.file, args.spec_version)
    if orbit_spec_version_number is not None:
        print(f"Using Orbit API spec version: {orbit_spec_version_number}")
    new_version_number = bump_package_version(part=args.part, allow_dirty=True)
    print(f"Bumped package to version: {new_version_number}")
    regenerate_message = regenerate_package()
    print(regenerate_message)
    update_readme()
    correct_line_endings()


if __name__ == "__main__":
    main()
