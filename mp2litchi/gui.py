"""
GUI Module
"""
# pylint: disable=import-error
import tkinter as tk
from os import getcwd
from os.path import dirname
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
from typing import Callable, Literal

from mp2litchi import mp2litchi


class FileMessages:
    """
    Class for inf, warning, error messages
    """

    def __init__(
            self,
            filename: str,
            info_messages: list[str],
            warning_messages: list[str],
            error_messages: list[str]):
        """
        Constructor

        Args:
            filename (str): The filename the messages refer to
            info_messages list(str): A list of info messages
            warning_messages list(str): A list of warning messages
            error_messages list(str): A list of error messages

        """

        self.filename = filename
        self.info_messages = info_messages.copy()
        self.warning_messages = warning_messages.copy()
        self.error_messages = error_messages.copy()

    def get_info(self) -> str | None:
        """
        Getter for info messages
        Returns:
            A string containing the filename and all info messages
            or None if no messages exist

        """

        if len(self.info_messages) == 0:
            return None
        ret = f"{self.filename}:\n"
        for info_message in self.info_messages:
            ret += f"{info_message}\n"
        return ret

    def get_warn(self) -> str | None:
        """
        Getter for warning messages
        Returns:
            A string containing the filename and all warning messages
            or None if no messages exist

        """

        if len(self.warning_messages) == 0:
            return None
        ret = f"{self.filename}:\n"
        for warning_message in self.warning_messages:
            ret += f"{warning_message}\n"
        return ret

    def get_error(self) -> str | None:
        """
        Getter for error messages
        Returns:
            A string containing the filename and all error messages
            or None if no messages exist

        """

        if len(self.error_messages) == 0:
            return None
        ret = f"{self.filename}:\n"
        for error_message in self.error_messages:
            ret += f"{error_message}\n"
        return ret


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

        file_messages = []
        filenames = self.get_files()
        for filename in filenames:
            infos, warnings, errors = mp2litchi.convert(filename)
            file_messages.append(
                FileMessages(
                    filename,
                    infos,
                    warnings,
                    errors
                )
            )
        for file_message in file_messages:
            info = file_message.get_info()
            warn = file_message.get_warn()
            error = file_message.get_error()
            if info is not None:
                self.show_info(
                    info=info
                )
            if warn is not None:
                self.show_warning(
                    warnings=warn
                )
            if error is not None:
                self.show_error(
                    error=error
                )

    def show_info(self, info: str):
        """
        Displays an Info window
        Args:
            info: The Info message to be shown

        """

        messagebox.showinfo(
            title='Info',
            message=info
        )

    def show_warning(self, warnings: str):
        """
        Displays a warning window
        Args:
            warnings: The warning message to be shown

        """

        messagebox.showwarning(
            title='Warning',
            message=warnings
        )

    def show_error(self, error: str):
        """
        Displays an error window
        Args:
            error: The error message to be shown

        """

        messagebox.showerror(
            title='Error',
            message=error
        )

    def render(self):
        """
        Renders the GUI
        """

        self.root.mainloop()
