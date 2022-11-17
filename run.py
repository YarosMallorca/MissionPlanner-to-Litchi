"""
Starts the Mission Planner to Litchi converter
"""
# pylint: disable=import-error
from mp2litchi.mp2litchi import welcome
from mp2litchi.gui import Gui

welcome()
gui = Gui()
gui.render()
