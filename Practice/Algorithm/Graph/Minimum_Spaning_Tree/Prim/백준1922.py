import sys
from heapq import heappop, heappush
sys.stdin = open("/Users/leesh/Documents/ComputerScience_Study/Practice/Algorithm/input.txt", 'r')
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
def prim(graph):
    start = 1
    visited = [False for _ in range(n+1)]
    visited[start] = True
    pq = []
    cost = 0
    for edge in graph[start]:
        heappush(pq, [edge[1], edge[0]])
    while pq:
        current_weight, current_vertex = heappop(pq)
        if visited[current_vertex]:
            continue
        cost += current_weight
        visited[current_vertex] = True
        for edge in graph[current_vertex]:
            heappush(pq, [edge[1], edge[0]])
    return cost
print(prim(graph))