
def insert_sort(a):
    # loop the array
    for i in range(1, len(a)):
        key = a[i]  # key is the NUM of AFTER
        j = i - 1  # j is the index of BEFORE num

        # sort by min to max:
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    return a


a = [31, 41, 59, 26, 41, 58]
a = insert_sort(a)
print(a)