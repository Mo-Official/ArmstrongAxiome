from dataclasses import dataclass
from typing import Iterable, List, MutableSequence, Tuple, Union
from src.models import Dependacy, Attribute, Side


class DependanciesManager:
    dependacies: List[Dependacy] = []
    derived_dependacies: List[Dependacy] = []

    def add(self, dependancy: Dependacy):
        """Adds a dependancy to the list"""
        if isinstance(dependancy, Dependacy) and not dependancy in self.dependacies:
            return self.dependacies.append(dependancy)
        if isinstance(dependancy, Iterable):
            for d in dependancy:
                self.add(d)

    def add_derived(self, dependancy):
        """Adds a dependancy to the deriviation list"""
        
        if isinstance(dependancy, Dependacy) and not dependancy in self.derived_dependacies:
            return self.derived_dependacies.append(dependancy)
        if isinstance(dependancy, MutableSequence):
            for d in dependancy:
                self.add_derived(d)
    
    def clear_derived(self):
        self.derived_dependacies.clear()

            
        


class AttributeManager:
    attributes: List[Attribute] = []

    def add(self, attribute: Attribute):
        """Adds an attribute to the list"""
        if not attribute in self.attributes:
            self.attributes.append(attribute)


class RulesManager:
    rules: list

    def __init__(self, ruleset) -> None:
        self.rules = ruleset

    def find_rule(self, d):
        """
        Finds a pattern in the dependancy and returns a rule or None.
        Loops through the set of the rules and returns the first one that has a matching criteria.
        """
        return [rule for rule in self.rules if rule["criteria"]["test"](d)]
 

    def run_rule_action(self, rule, dep):
        """Runs the function of the passed rule on the dependancy"""
        rule["action"](dep)
