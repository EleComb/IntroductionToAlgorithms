import numpy as np
import math


def square_matrix_multiply_recursive(A, B,
                                     L1,
                                     L2):
    n = int(L1[1]) - int(L1[0]) + 1
    d = math.floor(n / 2 - 1)  # the half length of matrix width/height minus one
    # if the matrix's length is 1, then set whose value
    C = np.zeros((n, n))
    if n <= 0:
        return
    if n == 1:
        C[n - 1, n - 1] = A[L1[3], L1[0]] * B[L2[3], L2[0]]
    else:
        A11 = [L1[0], L1[0] + d, L1[2], L1[2] + d]
        A12 = [int((L1[0] + L1[1] + 1) / 2), L1[1], L1[2], L1[2] + d]
        A21 = [L1[0], L1[0] + d, int((L1[2] + L1[3] + 1) / 2), L1[3]]
        A22 = [int((L1[0] + L1[1] + 1) / 2), L1[1], int((L1[3] + L1[2] + 1) / 2), L1[3]]
        B11 = [L2[0], L2[0] + d, L2[2], L2[2] + d]
        B21 = [L2[0], L2[0] + d, int((L2[2] + L2[3] + 1) / 2), L2[3]]
        B12 = [int((L2[0] + L2[1] + 1) / 2), L2[1], L2[2], L2[2] + d]
        B22 = [int((L2[0] + L2[1] + 1) / 2), L2[1], int((L2[2] + L2[3] + 1) / 2), L2[3]]
        C[0:d + 1, 0:d + 1] = square_matrix_multiply_recursive(A, B, A11, B11) + \
                              square_matrix_multiply_recursive(A, B, A12, B21)
        C[0:d + 1, int(n / 2):int(n / 2 + d + 1)] = square_matrix_multiply_recursive(A, B, A11, B12) + \
                                                    square_matrix_multiply_recursive(A, B, A12, B22)
        C[int(n / 2):int(n / 2 + d + 1), 0:d + 1] = square_matrix_multiply_recursive(A, B, A21, B11) + \
                                                    square_matrix_multiply_recursive(A, B, A22, B21)
        C[int(n / 2):int(n / 2 + d + 1), int(n / 2):int(n / 2 + d + 1)] = square_matrix_multiply_recursive(A, B, A21, B12) + \
                                                                          square_matrix_multiply_recursive(A, B, A22, B22)
    return C


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

# A = [[1,2,3,4], [2,1,3,4], [4,3,2,1], [1,3,2,4]]
# B = [[1,3,5,6], [3,5,1,6], [6,1,3,5], [5,1,6,3]]
L1 = [0, n-1, 0, n-1]
L2 = [0, n-1, 0, n-1]
ret = square_matrix_multiply_recursive(A, B, L1, L2)
print(ret)
