# # 백준 문제풀때, inf로 나오는거 INF로 바꿔야함
# import sys
# import heapq

# def dijkstra(g, s):
#     distances = [float('inf') for _ in range(len(g))]
#     distances[s] = 0
#     q = []
#     heapq.heappush(q, [distances[s], s])
#     while q:
#         cur_distance, cur_vertex = heapq.heappop(q)
#         if cur_distance > distances[cur_vertex]:
#             continue
#         for adjacent_vertex, weight in g[cur_vertex]:
#             adjacent_distance = cur_distance + weight
#             if distances[adjacent_vertex] > adjacent_distance:
#                 distances[adjacent_vertex] = adjacent_distance
#                 heapq.heappush(q, [adjacent_distance, adjacent_vertex])
#     return distances

# sys.stdin = open("./Algorithm/Graph/Shortest_Path/input.txt", 'r')
# v, e = map(int, input().split())
# g = [list() for i in range(v+1)]
# s = int(input())
# for _ in range(e):
#     u, v, w = map(int, input().split())
#     g[u].append([v,w])
# ans = dijkstra(g, s)
# print(ans)

import sys
import heapq

# sys.stdin = open("./Algorithm/Graph/Shortest_Path/input.txt", 'r')
# v, e = 
