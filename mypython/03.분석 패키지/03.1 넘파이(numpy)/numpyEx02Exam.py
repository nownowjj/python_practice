import numpy as np 

a = np.array([-1, 3, 2, -6, 3, 0])
b = np.array([3, 6, 1, 2, 0, 2])
A = np.reshape(a, [2, 3])
B = np.reshape(b, [3, 2])

print( '\n행렬 A' )
print( A )

print( '\n행렬 B' )
print( B )

result3_1 = np.matmul(A, B)
result3_2 = np.matmul(B, A)

print( '\n행렬 result3_1' )
print( result3_1 )

print( '\n행렬 result3_2' )
print( result3_2 )