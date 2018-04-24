import math


def merge_no_guard(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [None] * n1
    R = [None] * n2
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    i = 0
    j = 0
    # for k in range(p, r+1):
    while True:
        if L[i] <= R[j]:
            A[p + i + j] = L[i]
            i += 1
            if i == len(L): # No_guard
                A[p+i+j: p+len(R)+j] = R[j: len(R)]
                break
        else:
            A[p + i + j] = R[j]
            j += 1
            if j == len(R): # No_guard
                A[p+i+j: p+len(L)+j] = L[i: len(L)]
                break


A = [0, 0, 2, 5, 10, 1, 4, 7, 9, 0]
merge_no_guard(A, 2, 4, 8)
print(A)