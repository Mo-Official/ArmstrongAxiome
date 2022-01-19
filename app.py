import tkinter as tk

from src.interface.home import HomePage



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Armstrong Axiomes")
    root.resizable(width=False, height=False)
    app = HomePage(root)
    app.grid()
    tk.mainloop()