from typing import List
from .models import Dependacy, Side, Attribute

def fd_blocked_test(d,  *kwards, **kwargs):
    "checks if the state of a dependancy is blocked"
    return True if d.state == "blocked" else False

def fd_blocked_action(d,  *kwards, **kwargs):
    "reports that the dependancy can't be derived"
    return d

def fd_proven_test(d,  *kwards, **kwargs):
    "checks if the state of the dependancy is proven"
    return True if d.state == "proven" else False

def fd_proven_action(d,  *kwards, **kwargs):
    "reports that the dependancy has been proven"
    return d


def has_trivial(d: Dependacy, *kwards, **kwargs) -> bool:
    "Checks the triviality Armstrong Axiome. Returns True if d has trivial attributes"
    for l_a in d.left_side.attributes:
        if l_a.id in [x.id for x in d.right_side.attributes]: #FIXME: The need to check for id smells like bad design!!
            return True


def remove_trivial(d: Dependacy, *kwards, **kwargs) -> Dependacy:
    "removes trivial attributes from d's right side"
    new_r_side = Side([])
    for r_a in d.right_side.attributes:
        if not r_a.id in [x.id for x in d.left_side.attributes]:
            new_r_side.attributes.append(r_a)
    return Dependacy(d.left_side, new_r_side, d)


def already_exists(d: Dependacy, d_list:List[Dependacy], *kwards, **kwargs) -> Dependacy:
    "returns true if d is present in d_list"
    for owned_dependacy in d_list:
        if d == owned_dependacy:
            return True
    return False

def set_proven(d: Dependacy, *kwards, **kwargs) -> Dependacy:
    "sets the state of d to proven"
    return Dependacy(d.left_side, d.right_side, d.origin, state="proven")




def rightside_empty(d:Dependacy, d_list:List[Dependacy], *kwards, **kwargs):
    "Checks if the right_side of d is empty"
    if len(d.right_side.attributes) == 0:
        return True
    return False


def is_stuck(d, d_list, *kwards, **kwargs):
    """Returns True if none of the attributes on the left_side of d can determine any new attributes"""
    ls_d = set(d.left_side.attributes)
    for x in d_list:
        ls_x = set(x.left_side.attributes)
        rs_x = set(x.right_side.attributes)
        if ls_d.issuperset(ls_x):
            if len(rs_x.difference(ls_d))>0:
                return False
    return True

def set_blocked(d, d_list, *kwards, **kargs):
    """Sets d.state to blocked"""
    return Dependacy(d.left_side, d.right_side, d.origin, state="blocked")



def can_prove_something(d, d_list, *kwards, **kwargs):
    """Returns True if any of the attributes on the left_side of d can determine atleast one new attribute"""
    ls_d = set(d.left_side.attributes)
    for x in d_list:
        ls_x = set(x.left_side.attributes)
        rs_x = set(x.right_side.attributes)
        if ls_d.issuperset(ls_x):
            if len(rs_x.difference(ls_d))>0:
                return True
    return False

def modify_dependancy(d:Dependacy, d_list, *kwards, **kwargs):
    """Changes d.
    uses the nested function `find_subset_dependancy(d,d_list)` to find a dependancy x (where x.left_side is a partial set of d.left_side
    and x.right_side has atleast one Attribute that is not in d.left_side)

    Which means everything that is determined using x can be determined using d.
    Using that we add x.left_side.attributes to d.left_side.attributes
    """
    def find_subset_dependacy(d:Dependacy, d_list) -> Dependacy:
        #FIXME: ALSO NEED ORIGIN
        ls_d = set(d.left_side.attributes)
        for x in d_list:
            ls_x = set(x.left_side.attributes)
            rs_x = set(x.right_side.attributes)  
            if ls_d.issuperset(ls_x) and len(rs_x.difference(ls_d))>0:
                return x
    subset_dependacy = find_subset_dependacy(d, d_list)
    new_leftside = [] + d.left_side.attributes
    for a in subset_dependacy.right_side.attributes:
        if a not in d.left_side.attributes:
            new_leftside.append(a)

    return Dependacy(Side(new_leftside), d.right_side, origin=subset_dependacy, state="unknown")
