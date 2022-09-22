

adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], # 그래프 인접 리스트 
[5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]

N = len(adj_list)

visited = [False] * N # 정점 방문 여부 확인 용


def dfs(v):
    visited[v] = True # 정점 v방문 
    print(v, ' ', end=" ")
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w) # 정점 v에 인접한 정점으로 dfs() 재귀 호출 \
print('DPS 방문 순서:')
for i in range(N):
    if not visited[i]:
        dfs(i)

