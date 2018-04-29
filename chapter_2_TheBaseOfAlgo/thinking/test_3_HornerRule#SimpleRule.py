def horner_rule(A, x):
    y = 0
    for i in range(len(A)-1, -1, -1):
        y = A[i] + x*y
    return y

x = 5
A = [5, 2, 4, 7, 1, 3, 2, 6]
retn = horner_rule(A, x)
print(retn)


def simple_rule(A, x):
    y = 0
    for i in range(0, len(A)):
        y += A[i]*(x**i)
    return y


retn = simple_rule(A, x)
print(retn)