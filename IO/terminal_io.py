from io_interface import *

class terminal_io(io_interface):
    
    """docstring for terminal_io."""
    def __init__(self, arg):
        super(terminal_io, self).__init__()
        self.arg = arg
