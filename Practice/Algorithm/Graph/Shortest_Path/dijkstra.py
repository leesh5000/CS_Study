# Shortest Path Problem : dijkstra's Algorithm
# - 다익스트라는 모든 간선에 대한 정보가 있다고 가정
# - 방향 그래프에 대한 최소경로 (스패닝트리는 무방향그래프!)
# - 간선 정보를 이용하는 알고리즘 -> graph에 간선 정보 담기
# - 탐욕 알고리즘의 일종(?)

from heapq import heappop, heappush


def dijkstra(graph, start):
    # 시작 정점부터 각 정점까지의 거리를 담는 리스트, 처음엔 무한대로 초기화
    distances = {vertex: float('inf') for vertex in graph}
    # 시작노드의 거리는 0으로 초기화
    distances[start] = 0
    # 가장 거리가 짧은 정점들을 뽑아줄 우선순위 큐
    pq = []
    # 거리정보와 시작정점을 우선순위 큐에 넣고 시작
    heappush(pq, [distances[start], start])
    while pq:
        current_distance, current_vertex = heappop(pq)
        # 만약, 현재노드까지의 거리가 거리정보에 담긴 값보다 크면, 다음차례로 넘어간다.
        if current_distance > distances[current_vertex]:
            continue
        # 여기까지왔으면, 현재노드가 최적해이므로 현재 노드와 연결된 노드들을 큐에 넣어준다.
        # 간선의 개수만큼 - O(E)
        for adjacent_vertex, weight in graph[current_vertex].items():
            # 시작정점부터 인접정점까지의 거리 = 현재거리 + 거리비용
            adjacent_distance = current_distance + weight
            # 인접정점까지의 거리가 현재 거리정보에 있는 값보다 작을때만,
            # 우선순위 큐에 간선 정보를 삽입 - O(logE) -> O(E)*O(logE)=O(ElogE)
            if adjacent_distance < distances[adjacent_vertex]:
                distances[adjacent_vertex] = adjacent_distance
                heappush(pq, [adjacent_distance, adjacent_vertex])
    return distances


graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(graph, 'A'))
