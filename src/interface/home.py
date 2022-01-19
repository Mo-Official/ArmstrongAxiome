import tkinter as tk
from typing import Iterable

from ..other.custom_parser import parse_dependancy

from ..logic.models import Dependacy

from ..logic.rule_engine import RuleEngine
from ..logic.rules import RULES

from .components.console import Console

from .forms.input_form import InputForm
from .forms.check_form import CheckForm

from .view_models import BaseView

class HomePage(BaseView):
    def __init__(self, master) -> None:
        super().__init__(master=master)

    def define(self):
        self.input_form = InputForm(self)
        self.check_form = CheckForm(self)
        self.console = Console(self)
        self.rule_engine = RuleEngine([], RULES, self.console)

    def place_grid(self):
        self.input_form.grid(row=0,column=0)
        self.check_form.grid(row=1, column=0)
        self.console.grid(row=2,column=0)

    def update_dependancies(self, d_list):
        print(d_list)
        for d in d_list:
            self.rule_engine.dependancies.append(parse_dependancy(d))
        self.console.output_to_console(f"Extended dependancies by {len(d_list)} dependancies")
    
    def clear_inputs(self): # FIXME: Should remove attributes too
        """removes existing dependancies"""
        n_d = len(self.rule_engine.dependancies)
        self.rule_engine.dependancies.clear()
        self.console.output_to_console(f"Removed {n_d} dependancies")
        pass

    def update_attributes(self, a_str):
        self.console.output_to_console("updated Attributes using " + a_str)
        pass

    def clear_attributes(self):
        pass

    def check_dependancy(self, d):
        self.rule_engine.apply_rules(parse_dependancy(d))
        pass


