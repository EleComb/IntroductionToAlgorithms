
def square_matrix_multiply_recursive(A, B):
    n = len(A)
    C = [[0 for row in range(n)] for col in range(n)]
    if n == 1:
        C[0][0] = A[0][0]*B[0][0]
    else: ### wtf???
        C[0][0] = square_matrix_multiply_recursive(A[0][0], B[0][0]) + square_matrix_multiply_recursive(A[0][1], B[1][0])
        C[0][1] = square_matrix_multiply_recursive(A[0][0], B[0][1]) + square_matrix_multiply_recursive(A[0][1], B[1][1])
        C[1][0] = square_matrix_multiply_recursive(A[1][0], B[0][0]) + square_matrix_multiply_recursive(A[1][1], B[1][0])
        C[1][1] = square_matrix_multiply_recursive(A[1][0], B[0][1]) + square_matrix_multiply_recursive(A[1][1], B[1][1])

    return C


A = [[1,2], [2,1]]
B = [[1,3], [3,5]]
ret = square_matrix_multiply_recursive(A, B)
print(ret)
