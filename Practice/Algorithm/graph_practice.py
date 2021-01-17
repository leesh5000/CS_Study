# 1. BFS
def bfs(graph, start):
    visited = {vertex: False for vertex in graph}
    need_visited_queue = []
    need_visited_queue.append(start)
    while need_visited_queue:
        current_vertex = need_visited_queue.pop(0)
        if visited[current_vertex]:
            continue
        visited[current_vertex] = True
        print(current_vertex)
        for edge in graph[current_vertex]:
            next_vertex = edge[1]
            need_visited_queue.append(next_vertex)

def dfs(graph, start):
    visited = {vertex: False for vertex in graph}
    need_visited_stack = []
    need_visited_stack.append(start)
    while need_visited_stack:
        current_vertex = need_visited_stack.pop()
        if not visited[current_vertex]:
            visited[current_vertex] = True
            print(current_vertex)
            for edge in list(reversed(graph[current_vertex])):
                next_vertex = edge[1]
                need_visited_stack.append(next_vertex)

def dijkstra(graph, start):
    from heapq import heappush, heappop
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = []
    heappush(pq, [distances[start], start])
    while pq:
        current_distance, current_vertex = heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for weight, next_vertex in graph[current_vertex]:
            next_distance = current_distance + weight
            if next_distance > distances[next_vertex]:
                continue
            distances[next_vertex] = next_distance
            heappush(pq, [distances[next_vertex], next_vertex])
    print(distances)

def prim(graph, start):
    from heapq import heappush, heappop
    visited = {vertex: False for vertex in graph}
    visited[start] = True
    pq = []
    mst = []
    for weight, vertex in graph[start]:
        heappush(pq, [weight, start, vertex])
    while pq:
        current_weight, prev_vertex, current_vertex = heappop(pq)
        if visited[current_vertex]:
            continue
        visited[current_vertex] = True
        mst.append([current_weight, prev_vertex, current_vertex])
        for next_weight, next_vertex in graph[current_vertex]:
            heappush(pq, [next_weight, current_vertex, next_vertex])
    mst.sort()
    print(mst)
    return mst

def kruskal(graph, start):
    parents = {}
    ranks = {}
    mst = []
    def make_set(vertex):
        parents[vertex] = vertex
        ranks[vertex] = 0
    def find(vertex):
        if parents[vertex] != vertex:
            parents[vertex] = find(parents[vertex])
        return parents[vertex]
    def union(u, v):
        r1 = find(u)
        r2 = find(v)
        if ranks[r1] > ranks[r2]:
            parents[r2] = r1
        else:
            parents[r1] = r2
            if ranks[r1] == ranks[r2]:
                ranks[r2] += 1
    for vertex in graph:
        make_set(vertex)
    edges = []
    
    for vertex in graph:
        for edge in graph[vertex]:
            edge.append(vertex)
            edges.append(edge)
    edges.sort()
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append([weight, v, u])
    mst.sort()
    print(mst)
    return mst

graph = {
    'A': [[4, 'B'], [2, 'C'], [7, 'D']],
    'B': [[4, 'A'], [1, 'C'], [6, 'E']],
    'C': [[2, 'A'], [1, 'B'], [3, 'D'], [2, 'E'], [4, 'F']],
    'D': [[7, 'A'], [3, 'C'], [2, 'F']],
    'E': [[6, 'B'], [2, 'C'], [1, 'F']],
    'F': [[2, 'D'], [4, 'C'], [1, 'E']]
}

bfs(graph, 'A')
print()
dfs(graph, 'A')
print()
dijkstra(graph, 'A')
print()
prim(graph, 'A')
print()
kruskal(graph, 'A')