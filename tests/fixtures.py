"""TEST - Helpers
Helper functions and fixtures
"""

# # Native # #
from typing import List, Callable

# # Installed # #
import pytest

# # Project # #
from ideology_mashup.entities import Ideology, Ideologies
from ideology_mashup.methods import mashup_one
from ideology_mashup.const import IDEOLOGIES_FILE

IDEOLOGIES = [
    Ideology(
        name="socialism",
        prefix="social"
    ),
    Ideology(
        name="democracy"
    ),
    Ideology(
        prefix="anti"
    )
]

IDEOLOGIES_YAML = """
ideologies:
  - name: socialism
    prefix: social
  - name: democracy
  - prefix: anti
"""

INVALID_IDEOLOGIES_YAML = IDEOLOGIES_YAML + """
  - foo: bar
"""

IDEOLOGIES_MASHUP = {
    "Social-Democracy",
    "Anti-Democracy",
    "Anti-Socialism"
}


@pytest.fixture
def classes_to_dicts() -> Callable[[List], List[dict]]:
    def _parse(classes: List) -> List[dict]:
        return [cls.dict() for cls in classes]

    return _parse


@pytest.fixture
def ideologies() -> Ideologies:
    return IDEOLOGIES


@pytest.fixture
def ideologies_yaml() -> str:
    return IDEOLOGIES_YAML


@pytest.fixture
def ideologies_invalid_yaml() -> str:
    return INVALID_IDEOLOGIES_YAML


@pytest.fixture
def tmp_file_path(tmp_path) -> str:
    return (tmp_path / IDEOLOGIES_FILE).as_posix()


@pytest.fixture
def ideologies_yaml_file(ideologies_yaml, tmp_file_path) -> str:
    with open(tmp_file_path, "w") as file:
        file.write(ideologies_yaml)

    return tmp_file_path


@pytest.fixture
def ideologies_invalid_yaml_file(ideologies_invalid_yaml, tmp_file_path) -> str:
    with open(tmp_file_path, "w") as file:
        file.write(ideologies_invalid_yaml)

    return tmp_file_path


@pytest.fixture
def empty_yaml_file(tmp_file_path) -> str:
    with open(tmp_file_path, "w") as file:
        file.write("\n")

    return tmp_file_path


@pytest.fixture
def mashed_ideologies():
    return IDEOLOGIES_MASHUP
