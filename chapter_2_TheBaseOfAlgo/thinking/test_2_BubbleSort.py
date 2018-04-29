def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]


A = [5, 2, 4, 7, 1, 3, 2, 6]
bubble_sort(A)
print(A)