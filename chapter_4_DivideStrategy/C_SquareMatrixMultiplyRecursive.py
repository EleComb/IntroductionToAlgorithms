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
    n = int(a12) - int(a11) + 1
    d = math.floor(n/2-1) # the half length of matrix width/height minus one
    # if the matrix's length is 1, then set whose value
    C = np.zeros((n, n))
    if n <= 0:
        return
    if n == 1:
        C[n-1, n-1] = A[a22, a11] * B[b22, b11]
    else:
        C[0:d+1, 0:d+1] = square_matrix_multiply_recursive(A, B,
                                                   a11,                 a11 + d,        a21,                 a21 + d,
                                                   b11,                 b11 + d,        b21,                 b21 + d) + \
                      square_matrix_multiply_recursive(A, B,
                                                   int((a11+a12+1)/2),  a12,            a21,                 a21 + d,
                                                   b11,                 b11 + d,        int((b21+b22+1)/2),  b22)
        C[0:d+1, int(n/2):int(n/2+d+1)] = square_matrix_multiply_recursive(A, B,
                                                   a11,                 a11 + d,        a21,                 a21 + d,
                                                   int((b11+b12+1)/2),  b12,            b21,                 b21 + d) + \
                      square_matrix_multiply_recursive(A, B,
                                                   int((a11+a12+1)/2),  a12,            a21,                 a21 + d,
                                                   int((b11+b12+1)/2),  b12,            int((b21+b22+1)/2),  b22)
        C[int(n/2):int(n/2+d+1), 0:d+1] = square_matrix_multiply_recursive(A, B,
                                                   a11,                 a11 + d,        int((a21+a22+1)/2),  a22,
                                                   b11,                 b11 + d,        b21,                 b21 + d) + \
                      square_matrix_multiply_recursive(A, B,
                                                   int((a11+a12+1)/2),  a12,            int((a22+a21+1)/2),  a22,
                                                   b11,                 b11 + d,        int((b21+b22+1)/2),  b22)
        C[int(n/2):int(n/2+d+1), int(n/2):int(n/2+d+1)] = square_matrix_multiply_recursive(A, B,
                                                   a11,                 a11 + d,        int((a21+a22+1)/2),  a22,
                                                   int((b11+b12+1)/2),  b12,            b21,                 b21 + d) + \
                  square_matrix_multiply_recursive(A, B,
                                                   int((a11+a12+1)/2),  a12,            int((a22+a21+1)/2),  a22,
                                                   int((b11+b12+1)/2),  b12,            int((b21+b22+1)/2),  b22)
    return C


# A = np.array([[1, 2], [2, 1]])
# B = np.array([[1, 3], [3, 5]])
A = np.array([[1, 2, 3, 4, 1, 2, 3, 4],
              [3, 4, 1, 2, 1, 2, 3, 4],
              [2, 1, 3, 4, 1, 2, 3, 4],
              [4, 3, 2, 1, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4],
              [1, 2, 3, 4, 1, 2, 3, 4]])
B = np.array([[5, 6, 7, 8, 5, 6, 7, 8],
              [8, 7, 6, 5, 5, 6, 7, 8],
              [5, 6, 8, 7, 5, 6, 7, 8],
              [7, 8, 6, 5, 5, 6, 7, 8],
              [7, 8, 6, 5, 5, 6, 7, 8],
              [7, 8, 6, 5, 5, 6, 7, 8],
              [7, 8, 6, 5, 5, 6, 7, 8],
              [7, 8, 6, 5, 5, 6, 7, 8]])
n = 8

C = np.array([[0 for row in range(n)] for col in range(n)])
# A = [[1,2,3,4], [2,1,3,4], [4,3,2,1], [1,3,2,4]]
# B = [[1,3,5,6], [3,5,1,6], [6,1,3,5], [5,1,6,3]]
ret = square_matrix_multiply_recursive(A, B,
                                       0, n-1, 0, n-1,
                                       0, n-1, 0, n-1)
print(ret)

