import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import Button


root = tk.Tk()

button = Button(root, text="Start Attendance")
button.pack(side="top", pady=5)

# root.geometry('200x150')
root.state('zoomed')
root.mainloop()
