from .functions import *

CAN_PROVE_SOMETHING = {
    "name" : "CAN_PROVE_SOMETHING",
    "description": """a
    In each round the rules are applied, if there are attributes that we can determine using the leftside of the FD we remove them from out rightside and add them to our leftside.""",
    "test": can_prove_something,
    "action": modify_dependancy
} 

CANT_PROVE_ANYTHING = {
    "name" : "CANT_PROVE_ANYTHING",
    "description": """in each round the rules are applied, if there are no attributes left that we can determine using the leftside of the modified FD and the right side of the FD is still not empty. than this means we can't go any further and the FD can't be derived""",
    "test": is_stuck,
    "action": set_blocked
}


RIGHTSIDE_EMPTY = {
    "name" : "RIGHTSIDE_EMPTY",
    "description": """if the right side of the FD is empty. that means it can be derived""",
    "test": rightside_empty,
    "action": set_proven
}

ALREADY_EXISTS = {
    "name" : "ALREADY_EXISTS",
    "description": """If the FD is already known to use. we can safely set the state to proven""",
    "test": already_exists,
    "action": set_proven
}


FD_BLOCKED = {
    "name" : "FD_BLOCKED",
    "description": """the state ofdependancy gets blocked if it can't find any attributes that it can determine. in this case, it's safe to assume that it can't be derived""",
    "test" : fd_blocked_test,
    "action" : fd_blocked_action
}

FD_PROVEN = {
    "name" : "FD_PROVEN",
    "description": """When state of the dependancy is set to proven. then print out that its has been proven""",
    "test": fd_proven_test,
    "action" : fd_proven_action
}

HAS_TRIVIAL = {
    "name" : "HAS_TRIVIAL",
    "description" : """One of the Armstrong Axiomes. If an Attribute is on both sides of the dependancy. it can be removed from the right side""",
    "test": has_trivial,
    "action": remove_trivial
}

RULES = (
    CAN_PROVE_SOMETHING, 
    CANT_PROVE_ANYTHING,
    RIGHTSIDE_EMPTY,
    ALREADY_EXISTS,
    FD_BLOCKED,
    FD_PROVEN,
    HAS_TRIVIAL
)