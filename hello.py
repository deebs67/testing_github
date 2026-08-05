#
# Here is a simple Python script that rolls a dice and prints the result. It uses the numpy library to
# generate a random integer between 1 and 8 (inclusive).
import numpy as np

msg = "Roll a dice!"
print(msg)

print(np.random.randint(1,9))
