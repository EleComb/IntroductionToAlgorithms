from chapter_4_DivideStrategy import A_FindMaxCrossingSubarray

A = [-1, -2, -3, -4, -5]
r1, r2, r3 = A_FindMaxCrossingSubarray.find_maximum_subarray(A, 0, 4)
print(r1, r2, r3)   # 0, 0, -1
