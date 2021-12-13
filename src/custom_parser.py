"""
customer_parser.py contains all functions related to parsing input strings.
Attribute names must consist of only capital english letter A-Z

When passing Attributes to the parser the input string must have to following form:
"{A,B,C,D,E,F,G}"

When passing Dependancies to the parser to the input string must:
* use -> to isolate sides
* attributes 

"""

from sre_constants import error
from typing import List
from dataclasses import dataclass
from re import compile
from src.models import Dependacy, Side, Attribute


STRICT_MODE = True  # Turn off to stop raising errors


def parse_attributes(input_string) -> List[Attribute]:
    """Parse an input string to find attributes.
    Input string must be in the following Form:
    "{A,B,C,D,E,F,G}"
    returns a list of Attributes object
    """
    s = "{A,B,C,D,E,F,G}"

    def validate_input(input_string):
        unvalid_input = compile("\{([A-Z]\,)*([A-Z])\}")
        search_res, _ = unvalid_input.subn("", input_string)
        if search_res:
            if STRICT_MODE:
                raise error(f"Input {search_res} is invalid")
            else:
                print(f"Skipping ({input_string}) because it's invalid")
                return False
        else:
            return True

    if validate_input(input_string):
        return [Attribute(att) for att in input_string[1:-1].split(",")]


def parse_dependancy(input_string) -> Dependacy:
    """Parse an input string.
    Input string must be in the following Form:
    [A-Z]+->[A-Z]+
    returns a Dependacy object
    """

    def validate_input(input_string):
        unvalid_input = compile("[A-Z]+\-\>[A-Z]+")
        search_res, _ = unvalid_input.subn("", input_string)
        if search_res:
            if STRICT_MODE:
                raise error(f"Input {search_res} is invalid")
            else:
                print(f"Skipping ({input_string}) because it's invalid")
                return False
        else:
            return True

    # TODO: Check if each side has known attributes

    def parse_left_side(input_string):
        right_side_prg = compile("[A-Z]+\-\>")
        right_side_args = right_side_prg.findall(input_string)[0][:-2]
        return Side([Attribute(arg) for arg in right_side_args])

    def parse_right_side(input_string):
        left_side_prg = compile("\-\>[A-Z]+")
        left_side_args = left_side_prg.findall(input_string)[0][2:]
        return Side([Attribute(arg) for arg in left_side_args])

    if validate_input(input_string):
        return Dependacy(parse_left_side(input_string), parse_right_side(input_string))


if __name__ == "__main__":
    import pprint

    attribut_menge = "{A,B,C,D}"
    attributes = parse_attributes(attribut_menge)
    dependacies_menge = [
        "A->D",
        "BD->ED",
        "BC->H",
        "D->A",
        "H->DEF",
        "F->B",
        "E->C",
        "G->HF",
    ]
    dependacies = []
    for d in dependacies_menge:
        dependacies.append(parse_dependancy(d))
    print("Attributes are: ")
    pprint.pprint(attributes)
    print("Dependancies are: ")
    pprint.pprint(dependacies)
