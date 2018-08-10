

class io_interface:

    """docstring for interface."""
    def __init__(self):
        self.buttons = {}
        self.widgets = {}

    def SetTitle(self, title):
        self.title = title

    def AddLabel(self, text):
        self.widgets[text] = "label"

    def AddButton(self, text, callback):
        self.widgets[text] = "button"
        self.buttons[text] = callback

    def UpdateWindow(self):
        pass

    def ClearWindow(self):
        self.buttons = {}
        self.widgets = {}

    def SetVisible(self, visible=True):
        self.visible = visible
