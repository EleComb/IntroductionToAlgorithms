import math


def detect_sum(A, p, q, r, sum):
    n1 = q - p + 1
    n2 = r - q
    L = [None] * n1
    R = [None] * n2
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
    # print(L, R)
    i = j = 0
    for k in L:
        ret = [k2 for k2 in R if k+k2 == sum]
        if len(ret) > 0:
            return k, ret[0]
    return None, None

# A = [0, 0, 1, 2, 3, 4, 5, 6, 0]
# sum = 6
# ret = detect_sum(A, 2, 4, 7, sum)
# print(ret)


def detect_sum_tree(A, p, r, sum):
    if p < r:
        q = math.floor((p+r)/2)
        detect_sum_tree(A, p, q, sum)
        detect_sum_tree(A, q+1, r, sum)
        ret1, ret2 = detect_sum(A, p, q, r, sum)
        if ret1 is not None and ret2 is not None:
            return ret1, ret2
    return None, None


A = [1, 15, 53, 23, 14, 49, 37, 787, 43]
sum = 90
ret1, ret2 = detect_sum_tree(A, 0, len(A) - 1, sum)
if ret1 is not None or ret2 is not None:
    print(str(sum) + " = " + str(ret1) + " + " + str(ret2))