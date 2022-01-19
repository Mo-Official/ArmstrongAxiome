import tkinter as tk

class BaseView(tk.Frame):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master=master, *args, **kwargs)
        self.define()
        self.place_grid()

    def define(self):
        """Define Elements to be shown in the View"""
        pass

    def place_grid(self):
        """Place elements using the grid system"""
        pass

