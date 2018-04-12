#
# a1, a2 = 76, 89
#
# bin_a1, bin_a2 = bin(a1), bin(a2)
#
# # 7 bit    7 bit
# slice_a1, slice_a2 = bin_a1[2: len(bin_a1)], bin_a2[2: len(bin_a2)]
# slice_a1, slice_a2 = [ int( slice_a1 ) for slice_a1 in slice_a1], [ int( slice_a2 ) for slice_a2 in slice_a2]
#
# print(slice_a1)
# print(slice_a2)
#
# def sum_slice(a1, a2):
#     global i
#     carry = 0
#     result = [None] * len(a1)
#     for i in range(0, len(a1)):
#         if carry == 1:
#             a1[i] = a1[i] + carry
#         if int(a1[i]) + int(a2[i]) >= 2:
#             carry = 1
#             result[i] = (a1[i] + a2[i])%2
#             continue
#         carry = 0
#         result[i] = a1[i] + a2[i]
#     if carry == 1 :
#         result[i + 1] = carry
#     return result
#
#
# result = sum_slice(slice_a1, slice_a2)
#
# print(result)
