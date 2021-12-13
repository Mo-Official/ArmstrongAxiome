__doc__ = """
Preprossessing.py is a collection of functions that will
reduce provided dependancies into simpler ones before setting
"""

from typing import List, Optional
from src.models import Attribute, Dependacy, Side


def can_project(d: Dependacy) -> bool:
    if len(d.right_side.attributes) > 1:
        return True
    return False


def project(d: Dependacy) -> List[Dependacy]:
    return [Dependacy(d.left_side, Side([a_r]), d) for a_r in d.right_side.attributes]


def has_trivial(d: Dependacy) -> bool:
    for l_a in d.left_side.attributes:
        if l_a.id in [x.id for x in d.right_side.attributes]: #FIXME: The need to check for id smells like bad design!!
            return True


def remove_trivial(d: Dependacy) -> Dependacy:
    new_r_side = Side([])
    for l_a in d.left_side.attributes:
        if not l_a.id in [x.id for x in d.right_side.attributes]: #FIXME: The need to check for id smells like bad design!!
            new_r_side.attributes.append(l_a)

    return Dependacy(d.left_side, new_r_side, d)


def leftside_splittable(d: Dependacy) -> bool: 
    if len(d.left_side.attributes) > 1 and is_existent(d.origin) == False:
        return True
    return False


def leftside_split(d: Dependacy) -> List[Dependacy]:
    """
    Splits the left side of the dependancy to make it easier to find a solution.
    It's safe to use this because the system calls this only if the compined left_side doesn't help find anything

    BUG: Splitting a side of n attributes should return n lists of n-1 elements. The complexity is n!

    Example:
    If we are checking for AB->C and cant find it the d_manager.
    We start looking for A->C or B->C by splitting the leftside.

    Args:
        d (Dependacy): Dependancy to be split

    Returns:
        List[Dependacy]: A list of dependacy after the split.
        The origin of the new Dependancies is None because AB->C doesn't prove A->C but the other way around.
    """
    return [
        Dependacy(Side([a_l]), d.right_side, None) for a_l in d.left_side.attributes
    ]


def can_traverse(d: Dependacy, d_list: List[Dependacy]) -> bool:
    pass


def let_traverse(d: Dependacy, d_list: List[Dependacy]) -> List[Dependacy]:
    """Returns a list of dependancies that can be proven using the traverse axiome

    Args:
        d (Dependacy): Dependancy to be traversed
        d_list (List[Dependacy]): List to be traversed

    Returns:
        List[Dependacy]: A List of dependancies that of the origin d and what is proven by d
    """
    pass


def is_existent(d):
    """Check if the d_manager has the dependancy"""
    pass


def block(d):
    """Set the node's state to blocked"""
    pass


def solve(d):
    """Set the node's state to solved"""
    pass


def final_solved(d):
    """Checks to see if the final node has been solved"""
    pass


def final_blocked(d):
    """Checks if the final node has been blocked"""
    pass


def return_solved(d):
    """Call when solved"""
    pass


def return_unsolved(d):
    """Call when unsolved"""
    pass
