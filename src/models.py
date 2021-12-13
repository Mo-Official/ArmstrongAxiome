from dataclasses import dataclass
from typing import List, NoReturn, Optional



class Attribute:
    """A class for an Attribute of a DB Dependancy"""

    def __init__(self, _id: str) -> None:
        self.id = _id
        pass

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return '"' + self.__str__() + '"'

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Attribute):
            return True if __o.id == self.id else False
        return False


class Side:
    """A Side of a functional DB Dependancy"""

    def __init__(self, attributes: List[Attribute]) -> None:
        self.attributes = attributes

    def __str__(self) -> str:
        return "".join([str(a) for a in self.attributes])
    
    def __repr__(self) -> str:
        return '"' + self.__str__() + '"'
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Side):
            if self.attributes in __o.attributes and __o.attributes in self.attributes:
                return True
        return False



class Dependacy:
    """A functional DB Dependacy.
    Has a right and a left side."""

    def __init__(
        self, left_side: Side, right_side: Side, origin=None, state="unknown"
    ) -> None:  # FIXME: origin could be multiple dependancies
        self.left_side = left_side
        self.right_side = right_side
        self.origin = origin
        self.state=state

    def __str__(self) -> str:
        return f"{str(self.left_side)}->{str(self.right_side)}"

    def __repr__(self) -> str:
        return '"' + self.__str__() + '"'

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Dependacy):
            if self.left_side == __o.left_side and\
                self.right_side == __o.right_side:
                return True
        return False
