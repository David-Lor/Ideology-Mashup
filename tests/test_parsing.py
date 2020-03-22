"""TEST - Parsing
Test parsing the ideologies YAML file
"""

# # Installed # #
import pytest

# # Project # #
from ideology_mashup.methods import parse_ideologies


def test_parse(ideologies_yaml_file, ideologies, classes_to_dicts):
    parsed_ideologies = parse_ideologies(ideologies_yaml_file)
    assert classes_to_dicts(parsed_ideologies) == classes_to_dicts(ideologies)


def test_parse_empty(empty_yaml_file):
    parsed_ideologies = parse_ideologies(empty_yaml_file)
    assert parsed_ideologies == []


def test_parse_invalid(ideologies_invalid_yaml_file):
    with pytest.raises(AttributeError):
        parse_ideologies(ideologies_invalid_yaml_file)
