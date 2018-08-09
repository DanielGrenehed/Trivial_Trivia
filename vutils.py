
import sys

# cross version function mapping

if sys.version_info[0] == 3:
    def raw_input(x): # define raw_input for python3
        return input(x)
