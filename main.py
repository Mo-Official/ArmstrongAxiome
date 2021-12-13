import pprint
import tkinter as tk
from tkinter.constants import TRUE
import tkinter.scrolledtext as scrolledtext
from typing import List
from typing_extensions import ParamSpecKwargs
from debug import DEBUG_ATTRIBUTES, DEBUG_DEPENDANCIES, DEBUG_MODE
from src.models import Dependacy
from src.managers import AttributeManager, DependanciesManager, RulesManager

from src.rules import PRODUCTION_RULESET
from src.custom_parser import parse_attributes, parse_dependancy




class MainApplication(tk.Frame):
    def __init__(self, parent: tk.Tk, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.d_manger = DependanciesManager()
        self.a_manager = AttributeManager()
        self.r_manger = RulesManager(PRODUCTION_RULESET)


        self.run()

    def run(self):
        self.attributes_form()
        self.dependancy_form()
        self.checking_form()
        self.logging_console = scrolledtext.ScrolledText(
            self, state="disabled", width=60, background="black", fg="white"
        )

        def run_rules(): #FIXME: This should have its own form
            self.output_to_console("Starting...")
            for d in self.d_manger.dependacies:
                self.output_to_console(f"Working on: {d}")
                rules = self.r_manger.find_rule(d)
                while len(rules) > 0:
                    for r in rules:
                        self.output_to_console(f"Rule Matched: {r['name']}")
                        if r["criteria"]["test"](d) == r["criteria"]["must_return"]:
                            r['action'](d)
                            new_d = r['action'](d)
                            self.d_manger.add_derived(new_d)
                            self.output_to_console(f"New Dependancy {str(new_d)}")
                        else:
                            continue
                    rules = self.r_manger.find_rule(d)
                    

        self.run_rules_botton = tk.Button(
            self,
            text="Test Rule",
            command=run_rules
        )

        self.show_deps_botton = tk.Button(
            self,
            text="Show current Dependancies",
            command=lambda: self.output_to_console(f"{str(self.d_manger.dependacies)}")
        )

        self.show_derived_botton = tk.Button(
            self,
            text="Show Derived Dependancies",
            command=lambda: self.output_to_console(f"{str(self.d_manger.derived_dependacies)}")
        )

        if DEBUG_MODE:
            for a in parse_attributes(DEBUG_ATTRIBUTES):
                self.a_manager.add(a)
            for d in DEBUG_DEPENDANCIES:
                _d = parse_dependancy(d)
                _d.state = "proven"
                self.d_manger.add(_d)

        self.manage_grid()




    def manage_grid(self):
        """
        Layout is managed here
        Call always at the end of run
        """
        self.att_inputLabel.grid(row=0, column=0, padx=5, pady=5)
        self.att_inputEntry.grid(row=0, column=1, padx=5, pady=5)
        self.att_inputButton.grid(row=0, column=2, padx=5, pady=5)

        self.dep_inputLabel.grid(row=1, column=0, padx=5, pady=5)
        self.dep_inputEntry.grid(row=1, column=1, padx=5, pady=5)
        self.dep_inputButton.grid(row=1, column=2, padx=5, pady=5)

        self.check_inputLabel.grid(row=4, column=0, padx=5, pady=5)
        self.check_inputEntry.grid(row=4, column=1, padx=5, pady=5)
        self.check_inputButton.grid(row=4, column=2, padx=5, pady=5)

        self.run_rules_botton.grid(row=5, column=0, padx=5,pady=5)
        self.show_deps_botton.grid(row=6, column=0, padx=5,pady=5)
        self.show_derived_botton.grid(row=7, column=0, padx=5, pady=5)
        self.logging_console.grid(row=5, rowspan=10, column=1, columnspan=3)

    def checking_form(self):
        def submit_dependancy(v):
            "for now just logs to console"
            self.output_to_console(f"Idk if {parse_dependancy(v)} is valid")

        self.check_inputLabel = tk.Label(
            self, text="Input a dependancy to validate it"
        )
        self.check_inputEntry = tk.Entry(self)
        self.check_inputButton = tk.Button(
            self,
            text="Check",
            command=lambda: submit_dependancy(self.check_inputEntry.get()),
        )

    def attributes_form(self):
        def add_attributes(v):
            attributes = parse_attributes(v)
            for a in attributes:
                self.a_manager.add(a)
            self.output_to_console(f"Added {len(attributes)} new Attributes")

        self.att_inputLabel = tk.Label(self, text="Input attribute set")
        self.att_inputEntry = tk.Entry(self)
        self.att_inputButton = tk.Button(
            self,
            text="+",
            command=lambda: add_attributes(self.att_inputEntry.get()),
        )

    def dependancy_form(self):
        def add_dependancy(v):
            d = parse_dependancy(v)
            d.state = "proven"
            self.d_manger.add(d)
            self.output_to_console(f"Added {str(d)}")

        self.dep_inputLabel = tk.Label(self, text="Input a dependancy")
        self.dep_inputEntry = tk.Entry(self)
        self.dep_inputButton = tk.Button(
            self,
            text="+",
            command=lambda: add_dependancy(self.dep_inputEntry.get()),
        )

    def output_to_console(self, newText, end="\n"):
        """Logs newText to the console.
        https://stackoverflow.com/questions/66613428/tkinter-text-scroll-lag-issue
        Noticed that if the window is smaller than the console. scrolling will lag
        """
        self.logging_console["state"] = "normal"
        self.logging_console.insert("end", newText + end)
        self.logging_console["state"] = "disabled"


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Armstrong Axiomes")
    #root.geometry("580x650")
    root.resizable(width=False, height=False)
    print(root.winfo_geometry)
    app = MainApplication(root)
    app.grid()
    tk.mainloop()
