def split(L, k):
    a = []
    b = []
    for i in L:
        if i <= k:
            a.append(i)
        else:
            b.append(i)
            

    return a + b

L = [4, 2, 6, 1, 8, 5, 7, 2]

print(split(L, 3))

