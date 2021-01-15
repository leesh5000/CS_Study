# Prim's Algorithm
# - 시작 정점을 선택한 후, 정점에 인접한 간선 중 최소 간선으로 연결된 정점을 선택하고,
# 이를 반복하면서 신장 트리를 확장해나가는 방식

# Advanced Prim's Algorithm
# - 원래는 간선 정보를 우선순위 큐에 넣는데, 개선된 방식에서는 정점을 우선순위 큐에 넣는다.
# - 기본적인 프림 알고리즘의 경우 시간복잡도는 O(ElogE), 개선된 프림 알고리즘은 O(ElogV)

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
        # 모든 정점을 다 거치고 - O(E)
        for x in graph[current_node]:
            next_node = x[0]
            next_cost = x[1]
            # 정점 하나마다 힙에 데이터 삽입 - O(logV)
            heappush(pq, [next_cost, current_node, next_node])
    return mst

def prim2(graph, start):
    from heapdict import heapdict
    mst = []
    vertices = heapdict()
    memo = {}
    tot = 0
    # 처음에는 그래프의 모든 노드들을 돌면서, 각 노드들에 무한대, 어디서왔는지에는 None으로 초기화
    for vertex in graph.keys():
        vertices[vertex] = float('inf')
        memo[vertex] = None
    vertices[start], memo[start] = 0, start
    while vertices:
        vertex, key = vertices.popitem()
        mst.append([memo[vertex], vertex, key])
        tot += key
        for adjacent, weight in graph[vertex].items():
            if adjacent in vertices and weight < vertices[adjacent]:
                vertices[adjacent] = weight
                memo[adjacent] = vertex
    return mst, tot

g = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}

print(prim(g, 'A'))