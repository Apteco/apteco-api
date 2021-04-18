"""Tests for generator_script.py

Currently just testing ``fetch_and_update_spec()``
with the 5 different calling combinations of parameters, plus the error case.

"""
from unittest.mock import patch

import pytest

from gen.generator_script import fetch_and_update_spec


@patch("gen.generator_script.update_orbit_spec_version_number")
@patch("gen.generator_script.update_spec")
@patch("gen.generator_script.get_spec_from_file")
@patch("gen.generator_script.get_spec_from_api")
def test_1_spec_from_api(
    get_spec_from_api,
    get_spec_from_file,
    update_spec,
    update_orbit_spec_version_number,
):
    get_spec_from_api.return_value = ({"host": "apteco.com"}, "1.2.3.4567")

    version = fetch_and_update_spec(url="https://example1.com/OrbitAPI")

    assert version == "1.2.3.4567"
    get_spec_from_api.assert_called_once_with("https://example1.com/OrbitAPI")
    get_spec_from_file.assert_not_called()
    update_spec.assert_called_once_with({"host": "apteco.com"})
    update_orbit_spec_version_number.assert_called_once_with("1.2.3.4567")


@patch("gen.generator_script.update_orbit_spec_version_number")
@patch("gen.generator_script.update_spec")
@patch("gen.generator_script.get_spec_from_file")
@patch("gen.generator_script.get_spec_from_api")
def test_2_spec_from_file(
    get_spec_from_api,
    get_spec_from_file,
    update_spec,
    update_orbit_spec_version_number,
):
    get_spec_from_file.return_value = ({"host": "localhost"}, "1.3.5.79ac")

    version = fetch_and_update_spec(filepath="assets/api_specs/OrbitAPI-spec-1.3.5.79ac.json")

    assert version == "1.3.5.79ac"
    get_spec_from_api.assert_not_called()
    get_spec_from_file.assert_called_once_with("assets/api_specs/OrbitAPI-spec-1.3.5.79ac.json", None)
    update_spec.assert_called_once_with({"host": "localhost"})
    update_orbit_spec_version_number.assert_called_once_with("1.3.5.79ac")


@patch("gen.generator_script.update_orbit_spec_version_number")
@patch("gen.generator_script.update_spec")
@patch("gen.generator_script.get_spec_from_file")
@patch("gen.generator_script.get_spec_from_api")
def test_3_spec_from_file_supply_version(
    get_spec_from_api,
    get_spec_from_file,
    update_spec,
    update_orbit_spec_version_number,
):
    get_spec_from_file.return_value = ({"host": "127.0.0.1"}, "8.6.4.20")

    version = fetch_and_update_spec(filepath="data/api_specs/OrbitAPI-spec-latest.json", version="8.6.4.20")

    assert version == "8.6.4.20"
    get_spec_from_api.assert_not_called()
    get_spec_from_file.assert_called_once_with("data/api_specs/OrbitAPI-spec-latest.json", "8.6.4.20")
    update_spec.assert_called_once_with({"host": "127.0.0.1"})
    update_orbit_spec_version_number.assert_called_once_with("8.6.4.20")


@patch("gen.generator_script.update_orbit_spec_version_number")
@patch("gen.generator_script.update_spec")
@patch("gen.generator_script.get_spec_from_file")
@patch("gen.generator_script.get_spec_from_api")
def test_4_version_only(
    get_spec_from_api,
    get_spec_from_file,
    update_spec,
    update_orbit_spec_version_number,
):
    version = fetch_and_update_spec(version="my manual version")

    assert version == "my manual version"
    get_spec_from_api.assert_not_called()
    get_spec_from_file.assert_not_called()
    update_spec.assert_not_called()
    update_orbit_spec_version_number.assert_called_once_with("my manual version")


@patch("gen.generator_script.update_orbit_spec_version_number")
@patch("gen.generator_script.update_spec")
@patch("gen.generator_script.get_spec_from_file")
@patch("gen.generator_script.get_spec_from_api")
def test_5_no_update(
    get_spec_from_api,
    get_spec_from_file,
    update_spec,
    update_orbit_spec_version_number,
):
    version = fetch_and_update_spec()

    assert version is None
    get_spec_from_api.assert_not_called()
    get_spec_from_file.assert_not_called()
    update_spec.assert_not_called()
    update_orbit_spec_version_number.assert_not_called()


@patch("gen.generator_script.update_orbit_spec_version_number")
@patch("gen.generator_script.update_spec")
@patch("gen.generator_script.get_spec_from_file")
@patch("gen.generator_script.get_spec_from_api")
def test_error_both_url_and_filepath(
    get_spec_from_api,
    get_spec_from_file,
    update_spec,
    update_orbit_spec_version_number,
):
    with pytest.raises(ValueError) as exc_info:
        version = fetch_and_update_spec(
            url="https://example1.com/OrbitAPI",
            filepath="data/api_specs/OrbitAPI-spec-latest.json",
        )
    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Can only specify one of url or filepath"

    get_spec_from_api.assert_not_called()
    get_spec_from_file.assert_not_called()
    update_spec.assert_not_called()
    update_orbit_spec_version_number.assert_not_called()
