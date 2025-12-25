import numpy as np
a = np.ndarray(shape=(3,3), dtype=int)
a[:] = [[1,2,3],[4,5,6],[7,8,9]]
print("Matrix 1 elements are:\n", a)
print("Dimension of matrix 1 is:", a.ndim)
b = np.ndarray(shape=(3,3), dtype=int)
b[:] = [[1,3,4],[2,5,7],[3,5,9]]
print("Matrix 2 elements are:\n", b)
print("Dimension of matrix 2 is:", b.ndim)
print("Addition of 2 matrices:\n", np.add(a, b))
print("Subtraction of 2 matrices:\n", np.subtract(a, b))
print("Division of 2 matrices:\n", np.divide(a, b))
print("Matrix multiplication of 2 matrices:\n", np.dot(a, b))
