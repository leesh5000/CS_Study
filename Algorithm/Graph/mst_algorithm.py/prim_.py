# Prim vs Kruskal
# 크루스칼은 전체 간선들 중 최소 가중치, 프림은 현재까지 노드의 간선들 중 최소 가중치
# 둘 다 탐욕알고리즘을 기초
# Prim O(ElogE)

# import heapq

# # heapq.heapify 하면 한번에 힙 구조로 만들 수 있음
# g = [[2, 'A'], [5, 'B'], [3, 'C']]
# heapq.heapify(g)

# for i in range(len(g)):
#     print(heapq.heappop(g))

# # defaultdict 함수 사용
# from collections import defaultdict

# d = defaultdict(list)
# d2 = dict()
# print(d['name'])
# print(d2['name'])

from heapq import *
from collections import defaultdict

edges = [
    (7, 'A', 'B'),
    (5, 'A', 'D'),
    (8, 'B', 'C'),
    (9, 'B', 'D'),
    (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'),
    (6, 'D', 'F'),
    (8, 'E', 'F'),
    (9, 'E', 'G'),
    (11, 'F', 'G'),
]

def prim(start_node, edges):
    # 먼저, mst를 담을 리스트 생성
    mst = []
    # 인접간선들을 담을 딕셔너리 생성
    adjacent_edges = defaultdict(list)
    # 간선을 하나씩 돌면서
    for weight, n, v in edges:
        # 각 노드에 대한 모든 인접간선들을 adjacent_edges에 넣기
        adjacent_edges[n].append((weight, n, v))
        adjacent_edges[v].append((weight, v, n))
    
    # 연결된 노드를 담을 집합 자료구조
    connected_nodes = set(start_node)
    # start_node에 인접 간선들이 시작 후보
    candidate_edge = adjacent_edges[start_node]
    # 최소 가중치를 갖는 간선들을 뽑기 위해 heapify하기
    heapify(candidate_edge)

    # 후보 간선들이 비어있을 때까지 while문 돌기
    while candidate_edge:
        # 후보간선리스트에서 우선순위가 가장 높은 간선을 pop하기
        weight, n, v = heappop(candidate_edge)
        # v(현재간선과 연결된 인접정점)가 connected_nodes에 없다면,
        if v not in connected_nodes:
            # connected_nodes에 인접정점(v)를 추가하고
            connected_nodes.add(v)
            # mst에 간선정보를 업데이트하기
            mst.append((weight, n, v))

            # connected_nodes에 새로운 정점이 추가되었으므로, candidate_edges를 업데이트
            for edge in adjacent_edges[v]:
                # 뽑은 간선의 인접노드(v)가 connected_nodes에 없을때만,
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge, edge)

    return mst

# 개선된 프림 알고리즘
# 개선된 프림 알고리즘의 시간복잡도는 O(ElogV)
# 위에서 한 프림 알고리즘의 시간복잡도는 O(ElogE)
# 대부분의 경우 정점보다 간선이 더 많음
# 일반적인 프림알고리즘은 간선이 중심, 개선된 프림 알고리즘은 노드가 중심

# heapdict는 우선순위큐인데, 안의 데이터의 키 값이 바뀌어도 우선순위 큐를 유지하게 해줌
from heapdict import heapdict
def advanced_prim(graph, start):
    mst = list()
    # 노드들의 키 값을 담는 자료구조 keys
    keys = heapdict()
    # 어느 노드로 들어온 간선에서 키 값이 업데이트 되었는지 저장하는 자료구조
    pi = dict()
    total_weight = 0

    for node in graph.keys():
        # 먼저, 노드들의 키 값을 무한대로 만듦
        keys[node] = float('inf')
        # 어디서 업데이트 되었느지는 아직 None
        pi[node] = None

    # 처음 노드의 키값을 0, pi값은 start로 초기화
    keys[start], pi[start] = 0, start

    while keys:
        current_node, current_key = keys.popitem()
        mst.append([pi[current_node], current_node, current_key])
        total_weight += current_key

        # 그래프의 현재 노드 정보를 가져와서
        for adjacent, weight in graph[current_node].items():
            # 인접한 노드가 keys에 있고, 
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node
    
    return mst, total_weight

graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11},
}

mst, total_weight = advanced_prim(graph, 'A')
print('MST: {}, Total Weight: {}'.format(mst, total_weight) )
print(prim('A', edges))