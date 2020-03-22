"""METHODS
Core functions of the app
"""

# # Native # #
import random

# # Installed # #
import yaml

# # Project # #
from ideology_mashup.entities import Ideology, Ideologies, Strings


def parse_ideologies(file_path: str = "ideologies.yaml") -> Ideologies:
    """Parse the ideologies from the given YAML file path.
    :return: list of Ideology objects
    """
    ideologies: Ideologies = list()

    with open(file_path, "r") as file:
        file_content = file.read()

    file_parsed = yaml.safe_load(file_content)
    if file_parsed:
        parsed_ideologies = file_parsed.get("ideologies")

        if parsed_ideologies:
            for parsed_ideology in parsed_ideologies:
                ideologies.append(Ideology(**parsed_ideology))

    return ideologies


def mashup_one(prefix: str, name: str):
    """Join a prefix and a name split by a hyphen
    """
    return prefix.capitalize() + "-" + name.capitalize()


def mashup_ideologies(ideologies: Ideologies, shuffle: bool = False) -> Strings:
    """Mashup a given list of Ideology objectsm, returning all possible combinations.
    For a combination of 2 ideologies to be valid, one must have a name and the other one a prefix.
    :return: list of strings
    """
    mashups: Strings = list()

    for ideology_base in ideologies:
        for ideology_prefix in ideologies:
            name = ideology_base.name
            prefix = ideology_prefix.prefix
            if ideology_base is not ideology_prefix and name and prefix:
                mashups.append(mashup_one(prefix=prefix, name=name))

    if shuffle:
        random.shuffle(mashups)

    return mashups


def write_strings(strings: Strings, file_path: str = "mashed_ideologies.txt"):
    """Write the given list of strings to a file (one string per line)
    """
    with open(file_path, "w") as file:
        for string in strings:
            file.write(string + "\n")
