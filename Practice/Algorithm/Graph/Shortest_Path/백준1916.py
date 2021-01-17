import sys
from heapq import heappop, heappush
sys.stdin = open("/Users/leesh/Documents/ComputerScience_Study/Practice/Algorithm/input.txt", 'r')
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
start, end = map(int, input().split())
def dijkstra(graph, start, end):
    distances = [float('inf') for _ in range(n+1)]
    distances[start] = 0
    pq = []
    heappush(pq, [distances[start], start])
    while pq:
        current_distance, current = heappop(pq)
        if current_distance > distances[current]:
            continue
        for adjacent, weight in graph[current]:
            next_distance = current_distance + weight
            if next_distance < distances[adjacent]:
                distances[adjacent] = next_distance
                heappush(pq, [next_distance, adjacent])
    return distances[end]
print(dijkstra(graph, start, end))