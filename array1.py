import numpy as np
from math import *

#print(cos(0))

arr = np.array([1,2,3,4])
add = arr + 5
print(add)
sub = arr - 1
print(sub)
mul = arr * 5
print(mul)

x = np.where(arr % 2 == 0)
print(x)