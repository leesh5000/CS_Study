# 그래프 알고리즘 - 1
# 패스트캠퍼스 최단경로알고리즘 1번 강의
# 다익스트라 O(ElogE)

# 최단경로문제
# - 가중치 그래프를 기반으로 최소 가중치를 갖는 경로를 찾는 문제

# 최단경로문제의 종류
# 1. Single-Source and Single-Destination Shortest Path Problem
# - 특정 노드에서 출발, 특정 노드에 도착하는 가장 짧은 경로 찾기
# 2. Single-Source Shortest Path Problem
# - 특정 노드에서 출발, 다른 모든 노드에 도착하는 가장 짧은 경로 찾기
# 3. All-Pair Shortest Path Problem
# - 그래프의 전체 노드에 대한 최단경로를 찾는 문제

# 최단경로 알고리즘 : 다익스트라 알고리즘(Dijikstra's Algorithm)
# - 최단경로 알고리즘 중 가장 유명한 알고리즘
# - 최단경로 2번 문제에 해당하는 알고리즘

# 다익스트라 알고리즘 로직
# - 여러 구현방법이 있지만, 여기서는 우선순위 큐를 이용한 방법


# 다익스트라 알고리즘 구현

# 파이썬 라이브러리 Heapq를 이용하여 우선순위 큐 만들기
"""
import heapq

q = []
heapq.heappush(q, [2, 'A'])
heapq.heappush(q, [5, 'B'])
heapq.heappush(q, [7, 'C'])
heapq.heappush(q, [1, 'D'])

for i in range(len(q)):
    print(heapq.heappop(q))
"""

g = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5},
}

import heapq

def Dijkstra(graph, start):
    # distance에 초기 거리를 무한대로 삽입 (파이썬에서 float('inf')는 무한대)
    distances = {node: float('inf') for node in graph}
    # 시작노드의 거리는 0이니까 0
    distances[start] = 0
    # 우선순위 큐
    q = []
    # 먼저, 우선순위 큐의 시작값으로 이 노드의 현재까지의 거리와 이 노드를 넣기
    heapq.heappush(q, [distances[start], start])

    # 큐에 데이터가 없을때까지 반복, 파이썬은 굳이 len(q) != 0 할 필요없음
    while q:
        # 우선순위큐에서 노드 꺼내기
        current_distance, current_node = heapq.heappop(q)
        
        # 만약, 우선순위큐에서 꺼낸 노드의 거리가 현재 기록된 최소거리보다 크다면, 더 이상 거리정보를 업데이트할 필요가 없다.
        if current_distance > distances[current_node]:
            continue

        # 현재 노드의 인접노드와 가중치 가져오기
        for adjacent, weight in g[current_node].items():
            # 현재노드에서 인접노드까지 거리 = 현재 노드까지의 최소거리 + 인접노드 경로의 가중치
            adjacent_distance = current_distance + weight

            # 만약, 인접노드까지의 거리가 이전에 구했던 최소거리보다 더 작다면,
            if adjacent_distance < distances[adjacent]:
                # 거리를 업데이트
                distances[adjacent] = adjacent_distance
                # 지금까지 최소경로였으므로(최적해), 다음에도 최소경로를 구하기위해 큐에 삽입
                heapq.heappush(q, [adjacent_distance, adjacent])
                
    # 여기까지오면, start 노드부터 각 노드까지의 최단거리가 담긴다.
    return distances

print(Dijkstra(g, 'A'))