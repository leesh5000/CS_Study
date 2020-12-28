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

from heapdict import heapdict

def advanced_prim(graph, start_node):
    mst, keys, pi, total_weight = list(), heapdi


print(prim('A', edges))