# # Prim's Algorithm
# # - 시작 정점을 선택한 후, 정점에 인접한 간선 중 최소 간선으로 연결된 정점을 선택하고,
# # 이를 반복하면서 신장 트리를 확장해나가는 방식

# # Advanced Prim's Algorithm
# # - 원래는 간선 정보를 우선순위 큐에 넣는데, 개선된 방식에서는 정점을 우선순위 큐에 넣는다.
# # - 기본적인 프림 알고리즘의 경우 시간복잡도는 O(ElogE), 개선된 프림 알고리즘은 O(ElogV)

# from heapq import heappop, heappush
# v, e = map(int, input().split())
# graph = {i:[] for i in range(1,v+1)}
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph[a].append([b,c])
#     graph[b].append([a,c])
# def prim(graph, start):
#     visited = [False for i in range(v+1)]
#     visited[start] = True
#     pq = []
#     ans = 0
#     mst = []
#     for x in graph[start]:
#         next_node = x[0]
#         next_cost = x[1]
#         current_node = start
#         heappush(pq, [next_cost, current_node, next_node])
#     # 간선에 개수만큼 - O(E)
#     while pq:
#         current_cost, prev_node, current_node = heappop(pq)
#         if visited[current_node]:
#             continue
#         visited[current_node] = True
#         ans += current_cost
#         mst.append([current_cost, prev_node, current_node])
#         # 모든 정점을 다 거치고 - O(E)
#         for x in graph[current_node]:
#             next_node = x[0]
#             next_cost = x[1]
#             # 정점 하나마다 힙에 데이터 삽입 - O(logV)
#             heappush(pq, [next_cost, current_node, next_node])
#     return mst

# g = {
#     'A': {'B': 7, 'D': 5},
#     'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
#     'C': {'B': 8, 'E': 5},
#     'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
#     'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
#     'F': {'D': 6, 'E': 8, 'G': 11},
#     'G': {'E': 9, 'F': 11}
# }

# print(prim(g, 'A'))

# 프림 알고리즘
# - 크루스칼은 O(ElogE), 프림은 O(ElogV)
# - 프림은 노드와 우선순위 큐를 중심으로 알고리즘을 진행

# 프림 알고리즘
# 1. 시작 정점과 연결된 간선 중 가장 작은 간선과 연결
# 2. 모든 연결된 간선 중 가장 작은 간선을 연결, 단, 이미 방문한 정점인 경우에는 연결하지 않음
from heapq import heappush, heappop
def prim(graph, start):
    mst = []
    # 처음에 방문정보를 기록할 리스트를 생성, 시작정점은 방문으로 초기화
    visited = {node: False for node in graph}
    visited[start] = True
    # 간선들을 담을 우선순위 큐
    pq = []
    # 처음엔 시작정점과 연결된 간선들을 우선순위 큐에 넣기
    for edge in graph[start]:
        weight = edge[0]
        next = edge[1]
        heappush(pq, [weight, start, next])
    while pq:
        weight, prev, current = heappop(pq)
        if visited[current]:
            continue
        mst.append([weight, prev, current])
        visited[current] = True
        for edge in graph[current]:
            weight = edge[0]
            next = edge[1]
            heappush(pq, [weight, current, next])
    return mst
        
g = {
    'A': [[8, 'C'], [1, 'B'], [2, 'D']],
    'B': [[1, 'A'], [5, 'C'], [4, 'D']],
    'C': [[8, 'A'], [5, 'B']],
    'D': [[2, 'A'], [4, 'B']]
}

print(prim(g, 'A'))