

def square_matrix_multiply(A, B):
    n = len(A[0])
    C = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    return C


# A = [[1,2], [2,1]]
# B = [[1,3], [3,5]]
# ret = square_matrix_multiply(A, B)
# print(ret)

