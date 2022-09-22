import sys 
N = 4
INF = sys.maxsize
D = [[0, -2, INF, 1],
[INF, 0, 1, INF],
[1, INF, 0, INF], 
[INF, 2, 9, 0]]

for k in range(N): # 경유하는 정점 
    for i in range(N):
        for j in range(N):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

for i in range(N):
    for j in range(N):
        print('{0:3}'.format(D[i][j]), end='')
    print()