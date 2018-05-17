import numpy as np
import math


def strassen_algorithm(A, B, L1, L2):
    n = int(L1[1]) - int(L1[0]) + 1
    d = math.floor(n / 2 - 1)  # the half length of matrix width/height minus one
    # if the matrix's length is 1, then set whose value
    C = np.zeros((n, n))
    if n <= 0:
        return
    if n == 1:
        C[n - 1, n - 1] = A[L1[3], L1[0]] * B[L2[3], L2[0]]
    else:
        a11 = [L1[0], L1[0] + d, L1[2], L1[2] + d]
        a12 = [int((L1[0] + L1[1] + 1) / 2), L1[1], L1[2], L1[2] + d]
        a21 = [L1[0], L1[0] + d, int((L1[2] + L1[3] + 1) / 2), L1[3]]
        a22 = [int((L1[0] + L1[1] + 1) / 2), L1[1], int((L1[3] + L1[2] + 1) / 2), L1[3]]
        b11 = [L2[0], L2[0] + d, L2[2], L2[2] + d]
        b21 = [L2[0], L2[0] + d, int((L2[2] + L2[3] + 1) / 2), L2[3]]
        b12 = [int((L2[0] + L2[1] + 1) / 2), L2[1], L2[2], L2[2] + d]
        b22 = [int((L2[0] + L2[1] + 1) / 2), L2[1], int((L2[2] + L2[3] + 1) / 2), L2[3]]

        P1 = strassen_algorithm(A, B, a11, b12) - strassen_algorithm(A, B, a11, b22)
        P2 = strassen_algorithm(A, B, a11, b22) + strassen_algorithm(A, B, a12, b22)
        P3 = strassen_algorithm(A, B, a21, b11) + strassen_algorithm(A, B, a22, b11)
        P4 = strassen_algorithm(A, B, a22, b21) - strassen_algorithm(A, B, a22, b11)
        P5 = strassen_algorithm(A, B, a11, b11) + strassen_algorithm(A, B, a11, b22) + \
             strassen_algorithm(A, B, a22, b11) + strassen_algorithm(A, B, a22, b22)
        P6 = strassen_algorithm(A, B, a12, b21) + strassen_algorithm(A, B, a12, b22) - \
             strassen_algorithm(A, B, a22, b21) - strassen_algorithm(A, B, a22, b22)
        P7 = strassen_algorithm(A, B, a11, b11) + strassen_algorithm(A, B, a11, b12) - \
             strassen_algorithm(A, B, a21, b11) - strassen_algorithm(A, B, a21, b12)

        C[0:d + 1, 0:d + 1] = P5 + P4 - P2 + P6
        C[0:d + 1, int(n / 2):int(n / 2 + d + 1)] = P1 + P2
        C[int(n / 2):int(n / 2 + d + 1), 0:d + 1] = P3 + P4
        C[int(n / 2):int(n / 2 + d + 1), int(n / 2):int(n / 2 + d + 1)] = P5 + P1 - P3 - P7
    return C


n = 8
A = np.random.randint(0, 100, size=[n, n])
B = np.random.randint(0, 100, size=[n, n])

L1 = [0, n - 1, 0, n - 1]
L2 = [0, n - 1, 0, n - 1]
ret = strassen_algorithm(A, B, L1, L2)
# ret2 = np.dot(A, B)
# print(ret2)
print(ret)

