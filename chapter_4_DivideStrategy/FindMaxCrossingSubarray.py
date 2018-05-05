import math


def find_max_crossing_subarray(A, low, mid, high):
    global max_left, max_right
    left_sum = -math.inf
    sum = 0
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -math.inf
    sum = 0
    for j in range(mid+1, high+1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum

# A = [0, 0, -3, 6, 0]
# r1, r2, r3 = find_max_crossing_subarray(A, 2, 2, 3)
# print(r1, r2, r3)


def find_maximum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = math.floor((low+high)/2)
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


# A = [5, 6, -3, -8, 2, 5, -4, 5, 7, -9]
# r1, r2, r3 = find_maximum_subarray(A, 0, len(A)-1)
# print(r1, r2, r3)
