from pywinauto.application import Application
from subprocess import Popen
from pywinauto import Desktop
app = Application(backend="uia").start('notepad.exe')
# https://pywinauto.readthedocs.io/en/latest/getting_started.html

# describe the window inside Notepad.exe process
dlg_spec = app.UntitledNotepad
# wait till the window is really open
actionable_dlg = dlg_spec.wait('visible')



Popen('calc.exe', shell=True)
dlg = Desktop(backend="uia").Calculator
dlg.wait('visible')