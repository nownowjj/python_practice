import numpy as np

a = np.array([-1, 3, 2, -6])
b = np.array([3, 6, 1, 2])

print(a)
print(b)

A = np.reshape(a, [2, 2])
print(A)

B = np.reshape(b, [2, 2])
print(B)

result3_1 = np.matmul(A, B)
print(result3_1)

result3_2 = np.matmul(B, A)
print(result3_2)

b = np.reshape(b, [1, 4])
a = np.reshape(a, [1, 4])
b2 = np.transpose(b)
print(a)
print(b2)

result = np.matmul(a, b2)
print(result)
















