"""
Starts the Mission Planner to Litchi converter
"""
import tkinter as tk
from os import getcwd
from tkinter import filedialog as fd
from tkinter import ttk

from mp2litchi import mp2litchi

root = tk.Tk()
root.title('MP2Litchi')
root.resizable(False, False)
root.geometry('300x150')


def convert_files():
    """
    Opens the file select window and runs the conversion on each selected file.
    """
    filetypes = (
        ('text files', ['*.txt', '*.waypoints']),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Select files',
        initialdir=getcwd(),
        filetypes=filetypes)

    for filename in filenames:
        mp2litchi.convert(filename)


button = ttk.Button(
    root,
    text='Select files to convert',
    command=convert_files
)

button.pack(expand=True)


mp2litchi.welcome()
root.mainloop()
