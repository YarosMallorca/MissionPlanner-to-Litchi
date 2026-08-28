gui-assets:
	pyside6-rcc ./mp2litchi/gui_main_rc.qrc > ./mp2litchi/gui_main_rc_rc.py

gui: gui-assets
	pyside6-uic ./mp2litchi/gui_main.ui > ./mp2litchi/gui_main.py
