import numpy as np

def square_matrix_multiply(A, B):
    col = len(A)
    row = len(B[0])
    C = [[0 for row in range(row)] for col in range(col)]
    for i in range(col):
        for j in range(row):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C


# A = [[1, 2], [2, 1], [2, 5], [5, 2]]
# B = [[1, 3, 2], [3, 5, 9]]
# A = np.array(A)
# B = np.array(B)
# print(np.dot(A, B))
# ret = square_matrix_multiply(A, B)
# print(ret)

