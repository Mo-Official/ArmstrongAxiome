from src.axiomes import *

TRIVIAL = {
    "name": "TRIVIAL",
    "action": remove_trivial,
    "criteria": {"test": has_trivial, "must_return": True},
}

PROJECTION = {
    "name": "PROJECTION",
    "action": project,
    "criteria": {"test": can_project, "must_return": True},
}

LEFTSIDE_SPLIT = {
    "name": "LEFTSIDE_SPLIT",
    "action": leftside_split,
    "criteria": {"test": leftside_splittable, "must_return": True},
}

EXISTENCE = {
    "name": "EXISTENCE",
    "action": solve,
    "criteria": {"test": is_existent, "must_return": True},
}

NOT_EXISTENCE = {
    "name": "NOT_EXISTENCE",
    "action": block,
    "criteria": {"test": is_existent, "must_return": False},
}

FINAL_SOLVED = {
    "name": "FINAL_SOLVED",
    "action": return_solved,
    "criteria": {"test": final_solved, "must_return": True},
}

FINAL_BLOCKED = {
    "name": "FINAL_SOLVED",
    "action": return_unsolved,
    "criteria": {"test": final_blocked, "must_return": True},
}

PRODUCTION_RULESET = (
    TRIVIAL,
    PROJECTION,
    LEFTSIDE_SPLIT,
    EXISTENCE,
    NOT_EXISTENCE,
    FINAL_SOLVED,
    FINAL_BLOCKED,
)
