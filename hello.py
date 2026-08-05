#
# Here is a simple Python script that rolls a dice and prints the result. It uses the numpy library to
# generate a random integer between 1 and 8 (inclusive).
# This code comes from the very useful VSCode 'getting started' tutorial at:
# https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world

#
# Imports
import numpy as np

#
# Main 'business logic' of the script
msg = "Roll a dice!"
print(msg)

print(np.random.randint(1,9))

#
# That's it! You can run this script in VSCode by pressing F5 or by using the terminal.
#
