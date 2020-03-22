"""TOOLS - SORT IDEOLOGIES YAML
Override the ideologies.yaml file sorting the ideologies by:
1. Fields they have: name+prefix; name; prefix
2. Alphabetical order of name or prefix
"""

# # Installed # #
import yaml

# # Project # #
from ideology_mashup.methods import parse_ideologies
from ideology_mashup.entities import Ideology, Ideologies

IDEOLOGIES_INPUT_FILE = "ideologies.yaml"
IDEOLOGIES_OUTPUT_FILE = "ideologies.sorted.yaml"


def _sorter(ideology: Ideology):
    return (
        not bool(ideology.name and ideology.prefix),
        not bool(ideology.name),
        not bool(ideology.prefix),
        ideology.name,
        ideology.prefix
    )


def write_ideologies_yaml(ideologies: Ideologies):
    with open(IDEOLOGIES_OUTPUT_FILE, "w") as file:
        data = {"ideologies": [ideology.dict() for ideology in ideologies]}
        yaml.dump(data, file, default_flow_style=False)


def main():
    ideologies = parse_ideologies(IDEOLOGIES_INPUT_FILE)
    ideologies.sort(key=_sorter)
    write_ideologies_yaml(ideologies)


if __name__ == '__main__':
    main()
