#9.# CWE-400: Uncontrolled Resource Consumption
# This code creates a large array without checking its size, leading to potential memory exhaustion
import numpy as np

my_array = np.zeros((100000000, 100000000))