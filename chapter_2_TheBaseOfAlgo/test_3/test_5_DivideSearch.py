import math


# divide
def divide_search(a, p, r, v):
    q = math.floor((r-p)/2)
    if v == a[p]:
        return p
    if r - p <= 0:
        return None
    r1 = divide_search(a, p, p+q, v)
    r2 = divide_search(a, p+q+1, r, v)
    if r1 is not None:
        return r1
    if r2 is not None:
        return r2
    return None


# a = [12, 13, 210, 0]
a = [12, 13, 1, 35, 66, 210, 100, 150, 88]
v = 210
result = divide_search(a, 0, len(a)-1, v)
print(result)

v = 0
print(divide_search(a, 0, len(a)-1, v))

# # in python sugar:
# v = 210
# result = [ i for i in range(0, len(a)) if a[i] == v ]
# print(result[0])