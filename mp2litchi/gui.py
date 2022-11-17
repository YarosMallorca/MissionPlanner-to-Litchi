"""
GUI Module
"""
# pylint: disable=import-error
import tkinter as tk
from os import getcwd
from os.path import dirname
from tkinter import filedialog as fd
from tkinter import ttk
from typing import Callable, Literal

from mp2litchi import mp2litchi


class Gui:
    """
    Class for the GUI

    Attributes:
        current_dir (str): The directory the fileselector will start in
        root (Tk): The tkinter instance
    """

    def __init__(
            self,
            current_dir: str = getcwd(),
            title: str = 'MP2Litchi',
            width: int = 300,
            height: int = 150
    ):
        """
        Constructor

        Parameters:
            current_dir (str): The directory the fileselector will start in
            title (str): The test in the titlebar of the window
            width (int): The width of the window
            height (int): The height of the window
        """
        self.current_dir = current_dir
        self.root = tk.Tk()
        self.root.title(title)
        self.root.resizable(False, False)
        self.root.geometry(f"{width}x{height}")
        self.populate_gui()

    def populate_gui(self):
        """
        Method to bundle the setup of all the GUI elements
        """
        self.add_button(
            text='Select files to convert',
            callback=self.convert_files
        )

    def add_button(self, text: str, callback: Callable):
        """
        Adds a button to the GUI

        Parameters:
            text (str): The text to be displayed on the button
            callback (Callable): The callback function to be called when the button is clicked
        """
        button = ttk.Button(
            self.root,
            text=text,
            command=callback
        )
        button.pack(expand=True)

    def get_files(self) -> Literal[""] | tuple[str, ...]:
        """
        Opens the file select window

        Returns:
            List (Literal[""] | tuple[str, ...]): All selected filenames including their path
        """
        filetypes = (
            ('text files', ['*.txt', '*.waypoints']),
            ('All files', '*.*')
        )

        filenames = fd.askopenfilenames(
            title='Select files',
            initialdir=self.current_dir,
            filetypes=filetypes)
        if len(filenames) > 0:
            self.current_dir = dirname(filenames[0])
        return filenames

    def convert_files(self):
        """
        Convert all selected files
        """
        filenames = self.get_files()
        for filename in filenames:
            mp2litchi.convert(filename)

    def render(self):
        """
        Renders the GUI
        """
        self.root.mainloop()
