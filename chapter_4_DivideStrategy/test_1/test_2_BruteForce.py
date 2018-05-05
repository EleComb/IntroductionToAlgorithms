import math


def brute_force(A):
    max_sum = -math.inf
    ret_i = 0
    ret_j = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            sum = 0
            for k in range(i, j):
                sum += A[k]
            if sum > max_sum:
                max_sum = sum
                ret_i = i
                ret_j = j - 1
    return ret_i, ret_j, max_sum


# A = [-3, -2, 6, -5, 2, 6, -7, 3]
# r1, r2, r3 = brute_force(A)
# print(r1, r2, r3)

