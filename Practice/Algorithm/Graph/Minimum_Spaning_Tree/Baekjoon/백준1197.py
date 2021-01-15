# 런타임에러 이유 질문올린거 보기

import sys
sys.stdin = open('/Users/leesh/Documents/ComputerScience_Study/Practice/Algorithm/Graph/Minimum_Spaning_Tree/Baekjoon/input.txt', 'r')

""" Prim """
from heapq import heappop, heappush
v, e = map(int, input().split())
graph = {i:[] for i in range(1,v+1)}
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
def prim(graph, start):
    visited = [False for i in range(v+1)]
    visited[start] = True
    pq = []
    ans = 0
    mst = []
    for x in graph[start]:
        next_node = x[0]
        next_cost = x[1]
        current_node = start
        heappush(pq, [next_cost, current_node, next_node])
    # 간선에 개수만큼 - O(E)
    while pq:
        current_cost, prev_node, current_node = heappop(pq)
        if visited[current_node]:
            continue
        visited[current_node] = True
        ans += current_cost
        mst.append([current_cost, prev_node, current_node])
        # 최악의 경우에 모든 정점을 다 거치고 - O(E)
        for x in graph[current_node]:
            next_node = x[0]
            next_cost = x[1]
            # 정점 하나마다 힙에 데이터 삽입 - O(E) * O(logV)
            heappush(pq, [next_cost, current_node, next_node])
    return mst
print(sum([edge[0] for edge in prim(graph, 1)]))

# """ Prim """
# from heapq import heappop, heappush
# v, e = map(int, input().split())
# graph = {i:[] for i in range(1,v+1)}
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph[a].append([b,c])
#     graph[b].append([a,c])
# print(graph)
# def prim(graph, start):
#     visited = [False for i in range(v+1)]
#     visited[start] = True
#     pq = []
#     ans = 0
#     for x in graph[start]:
#         # edge = [weight, 현재노드, 다음에 방문할 노드]
#         # edge = [x[1], start, x[0]]
#         edge = [x[1], x[0]]
#         heappush(pq, edge)
#     while pq:
#         # current_cost, current_node, next_node = heappop(pq)
#         current_cost, current_node = heappop(pq)
#         if visited[current_node]:
#             continue
#         visited[current_node] = True
#         ans += current_cost
#         # mst.append([current_cost, current_node, next_node])
#         for x in graph[current_node]:
#             edge = [x[1], x[0]]
#             heappush(pq, edge)
#     return ans
# print(prim(graph, 1))

# """ Prim """
# from heapdict import heapdict
# v, e = map(int, input().split())
# graph = {i:{} for i in range(1,v+1)}
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#     graph[b][a] = c
# def prim(graph, start):
#     mst, keys, link = [], heapdict(), {}
#     for node in graph.keys():
#         keys[node] = float('inf')
#         link[node] = None
#     keys[start] = 0
#     link[start] = start
#     tot = 0
#     while keys:
#         current_node, key = keys.popitem()
#         mst.append([link[current_node], current_node, key])
#         tot += key
#         for adjacent_node, weight in graph[current_node].items():
#             if adjacent_node in keys and weight < keys[adjacent_node]:
#                 keys[adjacent_node] = weight
#                 link[adjacent_node] = current_node
#     return tot
# print(prim(graph, 1))


# """ Kruskal """
# graph = {
#     'vertices':[],
#     'edges':[]
# }
# v, e = map(int, input().split())
# for i in range(1, v+1):
#     graph['vertices'].append(i)
# for j in range(e):
#     edge = list(map(int, input().split()))
#     graph['edges'].append(edge)
# parents = {}
# ranks = {}
# def make_set(vertex):
#     parents[vertex] = vertex
#     ranks[vertex] = 0
# def find(vertex):
#     if parents[vertex] != vertex:
#         parents[vertex] = find(parents[vertex])
#     return parents[vertex]
# def union(u, v):
#     root1 = find(u)
#     root2 = find(v)
#     if ranks[root1] > ranks[root2]:
#         parents[root2] = root1
#     else:
#         parents[root1] = root2
#         if ranks[root1] == ranks[root2]:
#             ranks[root2] += 1
# def kruskal(graph):
#     weight = 0
#     for vertex in graph['vertices']:
#         make_set(vertex)
#     edges = graph['edges']
#     edges.sort()
#     for edge in edges:
#         w, u, v = edge
#         if find(u) != find(v):
#             union(u,v)
#             weight += w
#     return weight
# ans = kruskal(graph)
# print(ans)