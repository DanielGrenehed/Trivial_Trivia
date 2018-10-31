
import sys
from io_interface import *
import subprocess

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

# setup tkinter thread


class Tkinter_IO(io_interface):

    """docstring for tkinter_io."""
    def __init__(self):
        super().__init__()
        self.window  = tk.Tk()
        self.content = {}
        subprocess.self.window.mainloop() # into sepereate thread

    def SetCloseCallback(self, callback):
        self.window.protocol("WM_DELETE_WINDOW", callback)

    def CloseWindow(self):
        self.window.destroy()

    def __CreateWidget(self, k, v):
        if v == "label":
            self.content[k] = tk.Label(self.window, k)
        elif v == "button":
            self.content[k] = tk.Button(self.window, text=k, command=self.buttons[k])
        self.content[k].pack()

    def UpdateWindow(self):
        super(Tkinter_IO).Update_Window()
        for k, v in self.widgets.items():
            self.__CreateWidget(k, v)

    def ClearWindow(self):
        super(Tkinter_IO).ClearWindow()
        for k, v in self.content.items(): # delete widgets
            v.destroy()

    def SetVisible(self, visible=True):
        super(Tkinter_IO).SetVisible(visible)
        # set window visible
