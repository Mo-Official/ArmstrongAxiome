import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from typing import List
from src.managers import AttributeManager, DependanciesManager

from src.custom_parser import parse_attributes, parse_dependancy

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
        self.checking_form()
        self.att_listLabel = tk.Label(self.parent, text="Registered Attributes")
        self.dep_listLabel = tk.Label(self.parent, text="Registered Dependancies")
        self.att_list = tk.Listbox(self.parent)
        self.dep_list = tk.Listbox(self.parent)

        self.logging_console = scrolledtext.ScrolledText(self.parent, state="disabled", width=60, background="black", fg="white")

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

        self.att_listLabel.grid(row=2, column=0, padx=5, pady=5)
        self.att_list.grid(row=3, column=0)

        self.dep_listLabel.grid(row=2, column=1, padx=5, pady=5)
        self.dep_list.grid(row=3,column=1)

        self.check_inputLabel.grid(row=4, column=0, padx=5, pady=5)
        self.check_inputEntry.grid(row=4, column=1, padx=5, pady=5)
        self.check_inputButton.grid(row=4, column=2, padx=5, pady=5)

        self.logging_console.grid(row=5, column=0, columnspan=3)

    def checking_form(self):
        def submit_dependancy(v):
            "for now just logs to console"
            self.output_to_console(f"Idk if {parse_dependancy(v)} is valid")

        self.check_inputLabel = tk.Label(self.parent, text="Input a dependancy to validate it")
        self.check_inputEntry = tk.Entry(self.parent)
        self.check_inputButton = tk.Button(self.parent, text="Check", command=lambda: submit_dependancy(self.check_inputEntry.get()))
    
    def attributes_form(self):
        def add_attributes(v):
            attributes = parse_attributes(v)
            for a in attributes:
                self.a_manager.add(a)
                self.att_list.insert(len(self.a_manager.attributes),a)
            self.output_to_console(f"Added {len(attributes)} new Attributes")
        self.att_inputLabel = tk.Label(self.parent, text="Input attribute set")
        self.att_inputEntry = tk.Entry(self.parent)
        self.att_inputButton = tk.Button(self.parent, text="+", command=lambda: add_attributes(self.att_inputEntry.get()))

    def dependancy_form(self):
        def add_dependancy(v):
            d = parse_dependancy(v)
            self.d_manger.add(d)
            self.dep_list.insert(len(self.d_manger.dependacies),d)
            self.output_to_console(f"Added {str(d)}")
        self.dep_inputLabel = tk.Label(self.parent, text="Input a dependancy")
        self.dep_inputEntry = tk.Entry(self.parent)
        self.dep_inputButton = tk.Button(self.parent, text="+", command=lambda: add_dependancy(self.dep_inputEntry.get()))

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
    root.geometry("570x650")
    root.resizable(width=False, height=False)
    
    
    app = MainApplication(root)
    app.grid()
    tk.mainloop()