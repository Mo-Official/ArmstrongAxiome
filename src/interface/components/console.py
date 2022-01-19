import tkinter as tk
from ..view_models import BaseView

class Console(BaseView):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        
    def define(self):
        self.console_field = tk.Text(self, bg="black", fg="white", state="disabled")
        self.clear_button = tk.Button(self, text="Clear Console")
        pass
    
    def place_grid(self):
        self.clear_button.grid(row=0, column=0)
        self.console_field.grid(row=0,column=1)
        pass
        
    def output_to_console(self, text, end="\n"):
        self.console_field.config(state="normal")
        self.console_field.insert("end", "> "+text+end)
        self.console_field.config(state="disabled")

