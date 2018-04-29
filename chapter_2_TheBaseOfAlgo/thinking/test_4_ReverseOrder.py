import math

def reverse(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L1 = [None] * n1
    L2 = [None] * n2
    for i in range(n1):
        L1[i] = A[p + i]
    for j in range(n2):
        L2[j] = A[q + j + 1]
    i = j = 0
    while True:
        if L1[i] <= L2[j]:
            A[p + i + j] = L1[i]
            i += 1
            if i == n1:
                A[p+i+j:p+len(L2)+i] = L2[j:len(L2)]
                break
        else:
            pair.append([L1[i], L2[j]])
            # except that situation, add the Before number of OTHER reverse order value
            for k in range(i+1, n1):
                if L1[k] > L2[j]:
                    pair.append([L1[k], L2[j]])
            A[p + i + j] = L2[j]
            j += 1
            if j == n2:
                A[p+i+j:p+len(L1)+j] = L1[i:len(L1)]
                break

# pair = []
# A = [0, 0, 1, 4, 7, 2, 5, 6, 0]
# reverse(A, 2, 4, 7)
# print(A)
# print(pair)

def reverse_order(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        reverse_order(A, p, q)
        reverse_order(A, q+1, r)
        reverse(A, p, q, r)
        # print(pair)

pair = []
A = [3, 41, 52, 26, 38, 57, 9, 49]
# print(A)
reverse_order(A, 0, len(A)-1)
print(len(pair))
# print(A)
