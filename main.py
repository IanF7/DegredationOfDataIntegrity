# Ian Fletcher
# CST-305
# Degradation of Data Integrity over Time
# This is my own code

# imports necessary packages
import numpy as np
from matplotlib import pyplot as plt
import math


# creates functions for both equations
def equation1(t):
    return pow(math.e, -0.05 * t)


def equation2(t):
    return -(pow(math.e, -0.05 * t))


# creates two empty arrays to store y-values
eq1_y = []
eq2_y = []

# adds first 100 values of i passed into the equations to the end of eq1_y and eq2_y respectively
for i in range(100):
    eq1_y.append(equation1(i))
    eq2_y.append(equation2(i))
# generates x-values using np.linspace
x = np.linspace(1, 100, 100)
# plots results
plt.plot(x, eq1_y, 'b-', linewidth=1, label="Equation 1")
plt.plot(x, eq2_y, 'r-', linewidth=1, label="Equation 2")
plt.xlabel("Time")
plt.ylabel("Data Integrity")
plt.title("Data Integrity Over Time")
plt.legend()
plt.show()
