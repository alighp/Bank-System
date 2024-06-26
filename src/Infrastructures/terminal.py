import os

# ANSI escape code for setting foreground color to green
GREEN = "\033[32m"
# ANSI escape code for setting foreground color to red
RED = "\033[91m"
# ANSI escape code to reset foreground color
RESET = "\033[0m"    

def clear():
    if os.name == 'nt':  # windows
        os.system('cls')
    else:  # linux/mac
        os.system('clear') 