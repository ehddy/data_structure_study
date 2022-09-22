adj_list = [[1, 3, 4], [2, 6], [6],
[5], [3, 5], [], []] # 그래프 인접리스트 

N = len(adj_list)
visited = [False] * N # 정점 방문 여부 확인 용 
s = []

def dfs(v):
    visited[v] = True
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)
    s.append(v)


for i in range(N):
    if not visited[i]:
        dfs(i)

s.reverse()
print('위상정렬:')
print(s)