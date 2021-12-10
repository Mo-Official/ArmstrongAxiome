import tkinter as tk
from typing import List
from src.managers import AttributeManager, DependanciesManager

from src.ui import Homescreen
from src.custom_parser import parse_attributes, parse_dependancy
import logging



class MainApplication(tk.Frame):
    def __init__(self, parent:tk.Tk, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.d_manger = DependanciesManager()
        self.a_manager = AttributeManager()
        self.run()

    
    def run(self):

        self.attributes_form()
        self.dependancy_form()
        self.att_listLabel = tk.Label(self.parent, text="Registered Attributes")
        self.dep_listLabel = tk.Label(self.parent, text="Registered Dependancies")
        self.att_list = tk.Listbox(self.parent)
        self.dep_list = tk.Listbox(self.parent)
        
        self.logging_console = tk.Text(self.parent, state="disabled", width=60, background="black", fg="white")
        self.logging_console_scrollbar = tk.Scrollbar(self.parent, orient="vertical", command=self.logging_console.yview)
        self.logging_console.config(yscrollcommand=self.logging_console_scrollbar.set)

        self.temp_b1 = tk.Button(self.parent, text="Test logging 1", command=lambda: self.update_console("B"*300))
        self.temp_b2 = tk.Button(self.parent, text="Test logging 2", command=lambda: self.update_console("A"*120))
        self.manage_grid()

    def update_console(self, newText):
        """Logs newText to the console.

        Lines needs to be split into chunks to improve performance while scrolling.
        https://stackoverflow.com/questions/66613428/tkinter-text-scroll-lag-issue
        Also noticed that if the window is smaller than the console. scrolling will lag
        """
        line_length = 82
        lines = [newText[i:i+line_length] for i in range(0, len(newText), line_length)]
        self.logging_console["state"] = "normal"
        for line in lines:
            self.logging_console.insert("end", line+"\n")
        self.logging_console["state"] = "disabled"

    
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

        self.att_listLabel.grid(row=2, column=0, padx=5, pady=5)
        self.att_list.grid(row=3, column=0)

        self.dep_listLabel.grid(row=2, column=2, padx=5, pady=5)
        self.dep_list.grid(row=3,column=2)

        self.temp_b1.grid(row=4, column=0)
        self.temp_b2.grid(row=4, column=1)
        self.logging_console.grid(row=5, column=0, columnspan=3, sticky="nsew")
        self.logging_console_scrollbar.grid(row=5, column=3, sticky="nsew")

    
    def attributes_form(self):
        def add_attributes(v):
            attributes = parse_attributes(v)
            for a in attributes:
                self.a_manager.add(a)
                self.att_list.insert(len(self.a_manager.attributes),a)
        self.att_inputLabel = tk.Label(self.parent, text="Input attribute set")
        self.att_inputEntry = tk.Entry(self.parent)
        self.att_inputButton = tk.Button(self.parent, text="+", command=lambda: add_attributes(self.att_inputEntry.get()))

    def dependancy_form(self):
        def add_dependancy(v):
            d = parse_dependancy(v)
            self.d_manger.add(d)
            self.dep_list.insert(len(self.d_manger.dependacies),d)
        self.dep_inputLabel = tk.Label(self.parent, text="Input a dependancy")
        self.dep_inputEntry = tk.Entry(self.parent)
        self.dep_inputButton = tk.Button(self.parent, text="Submit Dependacy", command=lambda: add_dependancy(self.dep_inputEntry.get()))

    
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Armstrong Axiomes")
    root.geometry("570x650")
    root.resizable(width=False, height=False)
    
    
    app = MainApplication(root)
    app.grid()
    tk.mainloop()