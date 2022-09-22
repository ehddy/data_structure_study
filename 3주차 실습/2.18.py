def split(L):
    for i in range(1, len(L)):
        if L.count(i) == 2:
            return i







L = [1, 2, 4, 6, 5, 6, 3, 9, 8] 

print(split(L))