# 인접리스트를 이용해 그래프 구현
n, m, s = map(int, input().split())
g = {i:[] for i in range(n+1)}
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

def bfs(graph, start):
    visited = []
    need_visit = []
    need_visit.append(start)
    while need_visit:
        v = need_visit.pop(0)
        if v not in visited:
            need_visit.extend(sorted(graph[v]))
            print(v, end=' ')
            visited.append(v)

def dfs(graph, start):
    visited = []
    need_visit = []
    need_visit.append(start)
    while need_visit:
        v = need_visit.pop()
        if v not in visited:
            need_visit.extend(reversed(sorted(graph[v])))
            print(v, end=' ')
            visited.append(v)

dfs(g,s)
print()
bfs(g,s)
