import numpy as np
import math

# A = np.array([[1,2], [2,1]])
# B = np.array([[1,3], [3,5]])
# print(A + B)


# we should just use index of A, B . without more matrix
def square_matrix_multiply_recursive(A, B,
                                     a11,a12,a21,a22,
                                     b11,b12,b21,b22,
                                     c11,c12,c21,c22,depth=None):
    depth += 1
    # if the matrix's length is 1, then set whose value
    if depth == 2:
        C[c11, c11] = A[a11, a11] * B[b11, b11]
    else:
        C[0, 0] = square_matrix_multiply_recursive(A, B,
                                                   a11, math.floor((a11+a12)/2), a21, math.floor((a21+a22)/2),
                                                   b11, math.floor((b11+b12)/2), b21, math.floor((b21+b22)/2),
                                                   c11, math.floor((c11+c12)/2), c21, math.floor((c21+c22)/2),
                                                   depth) + \
                  square_matrix_multiply_recursive(A, B, 0, 0, depth)
        C[0, 1] = square_matrix_multiply_recursive(A[0][0], B[0][1]) + \
                  square_matrix_multiply_recursive(A[0][1], B[1][1])
        C[1, 0] = square_matrix_multiply_recursive(A[1][0], B[0][0]) + \
                  square_matrix_multiply_recursive(A[1][1], B[1][0])
        C[1, 1] = square_matrix_multiply_recursive(A[1][0], B[0][1]) + \
                  square_matrix_multiply_recursive(A[1][1], B[1][1])
    depth -= 1
    return C


A = np.array([[1,2], [2,1]])
B = np.array([[1,3], [3,5]])
n = 1
depth = 0

C = np.array([[0 for row in range(n)] for col in range(n)])
# A = [[1,2,3,4], [2,1,3,4], [4,3,2,1], [1,3,2,4]]
# B = [[1,3,5,6], [3,5,1,6], [6,1,3,5], [5,1,6,3]]
ret = square_matrix_multiply_recursive(A, B,
                                       0, n, 0, n,
                                       0, n, 0, n,
                                       0, n, 0, n,
                                       depth)
# print(ret)
