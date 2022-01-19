import tkinter as tk
from ..view_models import BaseView

class CheckForm(BaseView):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        
    def define(self):
        print("Input")
        self.check_label = tk.Label(self, text="Input dependancy to validate here: ")
        self.check_entry = tk.Entry(self)
        self.check_submit_button = tk.Button(self, text="Check", command=lambda: self.master.check_dependancy(self.check_entry.get())) # submit function needed
        pass
    
    def place_grid(self):
        self.check_label.grid(row=0, column=0)
        self.check_entry.grid(row=0, column=1)
        self.check_submit_button.grid(row=0, column=2)
    
    def get_question(self):
        return self.check_entry.get()