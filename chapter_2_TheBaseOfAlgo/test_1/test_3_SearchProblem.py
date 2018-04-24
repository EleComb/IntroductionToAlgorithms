# search by one loop
def search_problem(a, v):
    for i in range(len(a)) :
        if a[i] == v:
            return i
    return None


a = [12, 13, 1, 35, 66, 210, 100, 150, 88]
v = 210
result = search_problem(a, v)
print(result)

v = 0
print(search_problem(a,v))

# in python sugar:
v = 210
result = [ i for i in range(0, len(a)) if a[i] == v ]
print(result[0])