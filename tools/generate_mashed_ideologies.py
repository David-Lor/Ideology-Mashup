"""TOOLS - GENERATE MASHED IDEOLOGIES
"""

# # Project # #
from ideology_mashup.methods import parse_ideologies, mashup_ideologies, write_strings

IDEOLOGIES_FILE = "ideologies.yaml"
OUTPUT_FILE = "mashed_ideologies.txt"


def main():
    ideologies = parse_ideologies(IDEOLOGIES_FILE)
    mashed_ideologies = mashup_ideologies(ideologies, shuffle=False)
    write_strings(mashed_ideologies, OUTPUT_FILE)


if __name__ == '__main__':
    main()
