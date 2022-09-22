
# 1.9
s = 0
for i in range(3):
    for j in range(3):
        s += 3


# 1.11
r = 0 
for i in range(5):
    for j in range(i+1, 5+1):
        for k in range(j+1):
            r += 1 


def abc(N):
    if N <= 0:
        return 1

    return abc(N-1) + abc(N-2)
