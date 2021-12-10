from dataclasses import dataclass
from typing import List

@dataclass
class Attribute:
    """A class for an Attribute of a DB Dependancy"""
    def __init__(self, _id:str) -> None:
        self.id = _id
        pass
    
    def __str__(self) -> str:
        return self.id

@dataclass
class Side:
    """A Side of a functional DB Dependancy"""
    def __init__(self, attributes:List[Attribute]) -> None:
        self.attributes = attributes

    def __str__(self) -> str:
        return "".join([str(a) for a in self.attributes])

@dataclass
class Dependacy:
    """A functional DB Dependacy.
    Has a right and a left side."""
    def __init__(self, left_side:Side, right_side:Side) -> None:
        self.left_side = left_side
        self.right_side = right_side

    def __str__(self) -> str:
        return f"{str(self.left_side)} -> {str(self.right_side)}"
