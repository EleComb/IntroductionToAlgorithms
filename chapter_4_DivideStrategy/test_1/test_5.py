
def liner_time_maximum_subarray(A):
    index_sum = 0
    index_i = -1
    real_sum = 0
    # find the [0, i] maximum subarray
    for i in range(len(A)):
        index_sum += A[i]
        if index_sum > real_sum:
            real_sum = index_sum
            index_i = i

    # find the [j, i] maximum subarray
    index_sum = 0
    index_j = 0
    for j in range(index_i, -1, -1):
        index_sum += A[j]
        if index_sum > real_sum:
            real_sum = index_sum
            index_j = j
    return index_j, index_i, real_sum


A = [5, -8, 6, 7, 3, -7, -4, 2]
r1, r2, r3 = liner_time_maximum_subarray(A)
print(r1, r2, r3)