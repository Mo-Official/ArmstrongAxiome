from dataclasses import dataclass
from typing import List, Tuple, Union
from src.models import Dependacy, Attribute, Side


class DependanciesManager:
    dependacies:List[Dependacy] = []

    def find_related_dependancy(self, attribute:Union[Attribute, List[Attribute]]) -> List[Dependacy]:
        "Finds all dependancies that has the given attribute on the left side"
        return [d for d in self.dependacies if attribute in d.left_side.attributes]

    def find_full_dependant(self, attribute:Attribute) -> List[Dependacy]:
        """Finds all dependancies that has *only* the given attribute on the left side"""
        return [d for d in self.dependacies if [attribute] == d.left_side.attributes]

    def is_trivial(self, dep1:Dependacy) -> bool:
        """returns True if this depenancy is proven trivial
        Trivial dependancies should be removed"""
        if dep1.right_side.attributes in dep1.left_side.attributes:
            return True
        return False

    def is_extended(self, dep1:Dependacy, dep2:Dependacy) -> bool:
        """returns True if dep2 extends dep1"""
        pass

    def if_fully_dependant(self, att1:Attribute, att2:Attribute) -> bool:
        """returns True if attribute2 is fully dependant on att1"""
        pass

    def add(self, dependancy:Dependacy):
        """Adds a dependancy to the list"""
        if not dependancy in self.dependacies:
            self.dependacies.append(dependancy)


class AttributeManager:
    attributes:List[Attribute] = []

    def add(self, attribute:Attribute):
        """Adds an attribute to the list"""
        if not attribute in self.attributes:
            self.attributes.append(attribute)