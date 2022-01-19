import tkinter as tk
from ..view_models import BaseView


class InputForm(BaseView):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

    def define(self):
        self.attribute_label = tk.Label(self, text="Input Attributes here: ")
        self.default_attribute_input = tk.StringVar(self, value="{A,B,C,D,E,F,G,H}")
        self.attribute_entry = tk.Entry(self, textvariable=self.default_attribute_input)
        self.attribute_submit_button = tk.Button(
            self,
            text="+",
            command=lambda: self.master.update_attributes(self.attribute_entry.get()), # wacky design
        )

        self.depenancy_label = tk.Label(self, text="Input Dependancies here: ")
        self.dependancy_entry = tk.Text(self)
        self.dependancy_submit_button = tk.Button(
            self, text="+", command=lambda: self.master.update_dependancies(self.dependancy_entry.get("1.0","end").replace("\r","").strip().split("\n"))
        )  # submit function needed

        self.clear_button = tk.Button(self, text="Clear Input", command=lambda: self.master.clear_inputs())  # clear function needed

        pass

    def place_grid(self):
        self.attribute_label.grid(row=0, column=0)
        self.attribute_entry.grid(row=0, column=1)
        self.attribute_submit_button.grid(row=0, column=2)

        self.depenancy_label.grid(row=1, column=0)
        self.dependancy_entry.grid(row=1, column=1)
        self.dependancy_submit_button.grid(row=1, column=2)

        self.clear_button.grid(row=2, column=0)
