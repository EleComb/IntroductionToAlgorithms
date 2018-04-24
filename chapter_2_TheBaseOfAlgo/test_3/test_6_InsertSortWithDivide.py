import math


def divide_search_bound(A, p, r, v):
    if v < A[p]:
        return p-1
    if v > A[r]:
        return r
    tmp1, tmp2 = divide_search_middle(A, p, r, v)
    return tmp1


def divide_search_middle(A, p, r, v):
    q = math.floor((p+r)/2)
    if r - p < 1:
        return None, None
    elif r - p == 1:
        if A[p] <= v <= A[q]:
            return p, q
        if A[q] <= v <= A[r]:
            return q, r
    else:
        ret11, ret12 = divide_search_middle(A, p, q, v)
        ret21, ret22 = divide_search_middle(A, q, r, v)
        if ret11 is not None and ret12 is not None:
            return ret11, ret12
        elif ret21 is not None and ret22 is not None:
            return ret21, ret22
    return None, None


# A = [0, 0, 1, 6, 9, 10, 16, 34, 67, 99, 120, 0, 0]
# v = 20
# print(divide_search_middle(A, 2, 10, v))



def insert_sort(A):
    # loop the array
    for i in range(1, len(A)):
        key = A[i]  # key is the NUM of AFTER
        j = i - 1  # j is the index of BEFORE num

        # that's a problem... I can't set the Value when Merging
        # or first insert into 1st and mergeSort? that's maybe the solution
        idx1 = divide_search_bound(A, 0, i, key)
        for k in range(i - idx1 - 1):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key

    return A


a = [31, 41, 20, 26, 41, 58]
a = insert_sort(a)
print(a)