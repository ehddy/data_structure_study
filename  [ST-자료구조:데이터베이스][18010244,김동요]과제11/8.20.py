import sys
N = 5
s = 0
g = [None] * N
g[0] = [(1, 10), (3, 5)]
g[1] = [(2, 1), (3, 2)]
g[2] = [(4, 4)]
g[3] = [(1, 3), (2, 9), (4, 2)]
g[4] = [(0, 7), (2, 6)]


visited = [False] * N
D = [sys.maxsize] * N
D[s] = 0
previous = [None] * N
previous[s] = s 

for k in range(N):
    m = -1
    min_value = sys.maxsize
    for j in range(N):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j 
    visited[m] = True
    for w, wt in list(g[m]):
        if not visited[w]:
            if D[m]+wt < D[w]:
                D[w] = D[m] + wt 
                previous[w] = m

print('정점 ', s ,'(으)로부터 최단거리:')
for i in range(N):
    if D[i] == sys.maxsize:
        print(s, '와(과) ', i, ' 사이에 경로 없음.')
    else:
        print('({}, {})'.format(s, i), '=', D[i])

print()

print('정점 ', s, '(으)로부터 최단 경로:')
for i in range(N):
    back = i
    print(back, end='')
    while back != s:
        print(' <-', previous[back], end='')
        back = previous[back]
    print()