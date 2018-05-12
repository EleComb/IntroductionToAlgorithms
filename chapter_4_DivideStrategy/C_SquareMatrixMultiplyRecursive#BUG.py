import numpy as np
import math


# Test tools
# A = np.array([[1,2], [2,1]])
# B = np.array([[1,3], [3,5]])
# C = np.zeros((4, 4))
# C[0:2,0:2] = A
# print(C)
# print(A + B)


# we should just use index of A, B, C . without initial more matrix
def square_matrix_multiply_recursive(A, B,
                                     a11, a12, a21, a22,
                                     b11, b12, b21, b22):
    n = a12 - a11 + 1
    d = math.log2(n) - 1 # the half length of matrix width/height
    # if the matrix's length is 1, then set whose value
    if depth == 2:
        C[c11, c11] = A[a11, a11] * B[b11, b11]
    else:
        C[0, 0] = square_matrix_multiply_recursive(A, B,
                                                   a11, math.floor((a11 + a12) / 2), a21, math.floor((a21 + a22) / 2),
                                                   b11, math.floor((b11 + b12) / 2), b21, math.floor((b21 + b22) / 2)) + \
                  square_matrix_multiply_recursive(A, B, 0, 0)
        C[0, 1] = square_matrix_multiply_recursive(A[0][0], B[0][1]) + \
                  square_matrix_multiply_recursive(A[0][1], B[1][1])
        C[1, 0] = square_matrix_multiply_recursive(A[1][0], B[0][0]) + \
                  square_matrix_multiply_recursive(A[1][1], B[1][0])
        C[1, 1] = square_matrix_multiply_recursive(A[1][0], B[0][1]) + \
                  square_matrix_multiply_recursive(A[1][1], B[1][1])
    depth -= 1
    return C


A = np.array([[1, 2], [2, 1]])
B = np.array([[1, 3], [3, 5]])
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
