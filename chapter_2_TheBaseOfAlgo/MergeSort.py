import math
def merge(A, p ,q ,r):
    n1 = q - p + 1
    n2 = r - q
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    for i in range(n1 - 1):
        L[i] = A[p  + i - 1]
    for j in range(n2 - 1):
        R[j] = A[q + j]
    L[n1 + 1] = math.inf
    R[n2 + 1] = math.inf
    i = 1
    j = 1
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
        else:
            A[k] = R[j]
            j += 1
    return A

def merge_sort(A, p , r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(A, p, r)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A

A = [5,2,4,7,1,3,2,6]
print(merge_sort(A, 1, 3))