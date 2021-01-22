# # 1. BFS
# def bfs(graph, start):
#     visited = {vertex: False for vertex in graph}
#     need_visited_queue = []
#     need_visited_queue.append(start)
#     while need_visited_queue:
#         current_vertex = need_visited_queue.pop(0)
#         if visited[current_vertex]:
#             continue
#         visited[current_vertex] = True
#         print(current_vertex)
#         for edge in graph[current_vertex]:
#             next_vertex = edge[1]
#             need_visited_queue.append(next_vertex)

# def dfs(graph, start):
#     visited = {vertex: False for vertex in graph}
#     need_visited_stack = []
#     need_visited_stack.append(start)
#     while need_visited_stack:
#         current_vertex = need_visited_stack.pop()
#         if not visited[current_vertex]:
#             visited[current_vertex] = True
#             print(current_vertex)
#             for edge in list(reversed(graph[current_vertex])):
#                 next_vertex = edge[1]
#                 need_visited_stack.append(next_vertex)

# def dijkstra(graph, start):
#     from heapq import heappush, heappop
#     distances = {vertex: float('inf') for vertex in graph}
#     distances[start] = 0
#     pq = []
#     heappush(pq, [distances[start], start])
#     while pq:
#         current_distance, current_vertex = heappop(pq)
#         if current_distance > distances[current_vertex]:
#             continue
#         for weight, next_vertex in graph[current_vertex]:
#             next_distance = current_distance + weight
#             if next_distance > distances[next_vertex]:
#                 continue
#             distances[next_vertex] = next_distance
#             heappush(pq, [distances[next_vertex], next_vertex])
#     print(distances)

# def prim(graph, start):
#     from heapq import heappush, heappop
#     visited = {vertex: False for vertex in graph}
#     visited[start] = True
#     pq = []
#     mst = []
#     for weight, vertex in graph[start]:
#         heappush(pq, [weight, start, vertex])
#     while pq:
#         current_weight, prev_vertex, current_vertex = heappop(pq)
#         if visited[current_vertex]:
#             continue
#         visited[current_vertex] = True
#         mst.append([current_weight, prev_vertex, current_vertex])
#         for next_weight, next_vertex in graph[current_vertex]:
#             heappush(pq, [next_weight, current_vertex, next_vertex])
#     mst.sort()
#     print(mst)
#     return mst

# def kruskal(graph, start):
#     parents = {}
#     ranks = {}
#     mst = []
#     def make_set(vertex):
#         parents[vertex] = vertex
#         ranks[vertex] = 0
#     def find(vertex):
#         if parents[vertex] != vertex:
#             parents[vertex] = find(parents[vertex])
#         return parents[vertex]
#     def union(u, v):
#         r1 = find(u)
#         r2 = find(v)
#         if ranks[r1] > ranks[r2]:
#             parents[r2] = r1
#         else:
#             parents[r1] = r2
#             if ranks[r1] == ranks[r2]:
#                 ranks[r2] += 1
#     for vertex in graph:
#         make_set(vertex)
#     edges = []
    
#     for vertex in graph:
#         for edge in graph[vertex]:
#             edge.append(vertex)
#             edges.append(edge)
#     edges.sort()
#     for weight, u, v in edges:
#         if find(u) != find(v):
#             union(u, v)
#             mst.append([weight, v, u])
#     mst.sort()
#     print(mst)
#     return mst

# graph = {
#     'A': [[4, 'B'], [2, 'C'], [7, 'D']],
#     'B': [[4, 'A'], [1, 'C'], [6, 'E']],
#     'C': [[2, 'A'], [1, 'B'], [3, 'D'], [2, 'E'], [4, 'F']],
#     'D': [[7, 'A'], [3, 'C'], [2, 'F']],
#     'E': [[6, 'B'], [2, 'C'], [1, 'F']],
#     'F': [[2, 'D'], [4, 'C'], [1, 'E']]
# }

# bfs(graph, 'A')
# print()
# dfs(graph, 'A')
# print()
# dijkstra(graph, 'A')
# print()
# prim(graph, 'A')
# print()
# kruskal(graph, 'A')

# # BFS & DFS - 백준1260
# import sys
# sys.stdin = open("/Users/leesh/Documents/ComputerScience_Study/Practice/Algorithm/input.txt", 'r')
# n, m, start = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# def dfs(graph, start):
#     visited = [[] for _ in range(n+1)]
#     need_visit_stack = []
#     need_visit_stack.append(start)
#     while need_visit_stack:
#         cur_node = need_visit_stack.pop()
#         if visited[cur_node]:
#             continue
#         print(cur_node, end=' ')
#         visited[cur_node] = True
#         graph[cur_node].sort()
#         need_visit_stack.extend(list(reversed(graph[cur_node])))

# def bfs(graph, start):
#     visited = [[] for _ in range(n+1)]
#     need_visit_stack = []
#     need_visit_stack.append(start)
#     while need_visit_stack:
#         cur_node = need_visit_stack.pop(0)
#         if visited[cur_node]:
#             continue
#         print(cur_node, end=' ')
#         visited[cur_node] = True
#         graph[cur_node].sort()
#         need_visit_stack.extend(graph[cur_node])

# dfs(graph, start)
# print()
# bfs(graph, start)

# # dijkstra - 백준1753번. 최단경로
# import sys
# from heapq import heappop, heappush
# sys.stdin = open("/Users/leesh/Documents/ComputerScience_Study/Practice/Algorithm/input.txt", 'r')
# n, e = map(int, input().split())
# k = int(input())
# INF = float('inf')
# graph = [[] for _ in range(n+1)]
# for _ in range(e):
#     u, v, w = map(int, input().split())
#     graph[u].append([v, w])
# def dijkstra(graph, start):
#     distances = [INF for _ in range(n+1)]
#     pq = []
#     distances[start] = 0
#     heappush(pq, [distances[start], start])
#     while pq:
#         cur_distance, cur_node = heappop(pq)
#         if cur_distance > distances[cur_node]:
#             continue
#         distances[cur_node] = cur_distance
#         for next_node, next_weight in graph[cur_node]:
#             next_distance = cur_distance + next_weight
#             if next_distance > distances[next_node]:
#                 continue
#             distances[next_node] = next_distance
#             heappush(pq, [next_distance, next_node])
#     return distances
# ans = dijkstra(graph, k)
# for x in ans[1:]:
#     if x==INF:
#         print("INF")
#     else:
#         print(x)

# prim - 백준
import sys
from heapq import heappush, heappop
sys.stdin = open("/Users/leesh/Documents/ComputerScience_Study/Practice/Algorithm/input.txt", 'r')
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
def prim(graph, start):
    mst = []
    visited = [False for _ in range(v+1)]
    pq = []
    visited[start] = True
    for vertex, weight in graph[start]:
        heappush(pq, [weight, start, vertex])
    while pq:
        cur_weight, prev_node, cur_node = heappop(pq)
        if visited[cur_node]:
            continue
        visited[cur_node] = True
        mst.append([cur_weight, prev_node, cur_node])
        for next_node, next_weight in graph[cur_node]:
            heappush(pq, [next_weight, cur_node, next_node])
    return mst
ans = 0
for a,b,c in prim(graph, 1):
    ans += a
print(ans)
