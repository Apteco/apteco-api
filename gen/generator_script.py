"""
Script to re-generate the ``apteco-api`` package
based on the API spec at the given source.

This only generates the Python source code;
it does *not* then build a distribution from it or publish it to PyPI.

"""

import json
import shutil
import subprocess
from pathlib import Path

import parse
import semver
from urlpath import URL

API_BASE_URL = "https://www.tealgreenholidays.co.uk/OrbitAPI"
SPEC_SOURCE_PATH = "swagger/v2/swagger.json"
SPEC_OUTPUT_PATH = "gen/api-spec.json"
INTRODUCTION_PATH = "introduction.md"
README_PATH = "README.md"


def update_swagger_spec(
        spec_output_path=SPEC_OUTPUT_PATH,
        api_base_url=API_BASE_URL,
        spec_source_path=SPEC_SOURCE_PATH,
):
    """Update the API spec using the spec at the given source."""
    spec_url = URL(api_base_url) / spec_source_path
    spec_response = spec_url.get()
    spec = spec_response.json()

    spec.update({"host": "example.com", "basePath": "/OrbitAPI/"})

    spec_output_path = Path(spec_output_path)
    with open(spec_output_path, "w") as f:
        f.write(json.dumps(spec, indent=4))


def fetch_orbit_spec_version_no(api_base_url=API_BASE_URL):
    """Get the Orbit API spec version number from the given source."""
    spec_version_url = URL(api_base_url) / "About/Version"
    spec_version_response = spec_version_url.get()
    spec_version = spec_version_response.json().get("version")
    if spec_version is None:
        raise LookupError("Failed to fetch OrbitAPI spec version number.")
    else:
        return spec_version


def find_line_no(content_lines, match_text, error_message):
    """Find line number where given content occurs."""
    for line_no, line in enumerate(content_lines):
        if line.startswith(match_text):
            return line_no
    else:
        raise LookupError(error_message)


def update_orbit_spec_version_number(introduction_path=INTRODUCTION_PATH):
    """Write new Orbit API spec version number into README content."""
    with open(introduction_path, "r") as f:
        introduction_content = f.readlines()
    line_no = find_line_no(
        introduction_content,
        "- OrbitAPI spec version:",
        "Couldn't find where to change OrbitAPI spec version number in Introduction."
    )
    new_version = fetch_orbit_spec_version_no()
    introduction_content[line_no] = f"- OrbitAPI spec version: {new_version}\n"

    with open(introduction_path, "w") as f:
        f.writelines(introduction_content)


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
    if part not in ["major", "minor", "patch"]:
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


def generate_new_package():
    """Run package generator process and return result."""
    args = [
        r"java -jar gen\openapi-generator-cli-4.0.1.jar generate",
        r"-i gen\api-spec.json",
        r"-g python",
        r"-o .",
        r"-c gen\config.yaml",
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
        "[main] WARN  o.o.c.languages.PythonClientCodegen - Property (reserved word) cannot be used as model name. Renamed to ModelProperty",
        "[main] WARN  o.o.codegen.DefaultCodegen - Multiple MediaTypes found, using only the first one",
    ]
    OTHER_WARNINGS = [
        "[main] WARN  o.o.c.languages.PythonClientCodegen - Type object not handled properly in setParameterExampleValue",
        "[main] WARN  o.o.c.languages.PythonClientCodegen - Type list not handled properly in setParameterExampleValue",
        "[main] INFO  o.o.codegen.DefaultGenerator - Model ReferenceVariableInfo not generated since it's a free-form object",
    ]
    STANDARD_INFO = [
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
    remaining = []
    for line in significant:
        result = parse.parse(GENERATOR_IGNORE_FORMAT, line)
        if result is not None:
            skips.append(result["file_path"])
        else:
            remaining.append(line)

    message = ""
    if remaining:
        message += "Running the generator produced the following unrecognised log messages:\n"
        message += "\n".join(remaining)
    if skips:
        message += "The following files were skipped based on the .openapi-generator-ignore rules:\n"
        message += "\n".join(skips)

    return message


def regenerate_package():
    """Delete old package, generate new version and check output."""
    delete_old_package()
    result = generate_new_package()
    return check_generator_output(result)


def main():
    update_swagger_spec()
    update_orbit_spec_version_number()
    new_version_number = bump_package_version(part="minor", allow_dirty=True)
    print(f"Bumped package to version: {new_version_number}")
    regenerate_message = regenerate_package()
    print(regenerate_message)
    update_readme()


if __name__ == "__main__":
    main()
