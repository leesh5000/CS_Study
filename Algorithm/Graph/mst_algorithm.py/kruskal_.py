# 패스트캠퍼스 - 최소신장트리 강의
# Spanning Tree
# - 원래 그래프의 모든 노드가 연결되어있으면서 트리의 속성을 만족(즉, 사이클이 없음)

# Minimum Spannig Tree (MST)
# - 가능한 Spanning Tree 주에서, 간선의 가중치의 합이 최소인 Spanning Tree

# 그래프에서 MST를 찾는 알고리즘은 대표적으로 2개가 존재
# Kruskal's Algorithm, Prim's Algorithm

# Kruskal's Algorithm에서 사이클 여부를 판단하기 위해 Union-Find 자료구조의 Find 알고리즘을 활용할 수 있다.

# Union-Find Data Structure
# - Disjoint Set을 표현할 때 사용하는 트리 기반 자료구조
# - Disjoint Set이란, 서로 중복되지 않는 부분집합들로 이루어진 원소들에 대한 정보를 저장하고 조작하는 자료구조
# - 즉, Disjoint Set = 서로소 집합 자료구조
# - Init : n개의 원소가 개별집합으로 이뤄지도록 초기화하는 연산
# - Union : 서로 다른 두 개의 부분집합에 대한 합치는 연산 -> 두 개의 트리를 하나의 트리로 만듦
# - Find : 하나의 원소가 어떤 집합에 속해있는지를 판단하는 연산 -> 두 개의 노드에 대해서 각 노드가 속한 트리의 루트노드만 확인하면 서로 같은 집합인지 아닌지를 확인할 수 있음 -> 즉, 같은 트리안에 있는 것을 연결한다면 이것은 사이클을 이루게 됨

# Kruskal's Algorithm Using Union-Find 로직 구현
# 1. 모든 정점을 독립적인 집합으로 만든다.
# 2. 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 해당 간선의 두 정점을 뽑는다.
# 3. 두 정점의 최상위 정점을 확인하고(Find), 서로 다른경우 연결(Union) 같으면 버림
# 탐욕알고리즘을 기반으로 하고있다.
# 시간복잡도 = O(ElogE)

# 최적화 된 Union-Find 로직
# - Union-Find에서는 트리를 어떻게 구성해야하는지가 중요 (균형잡힌 트리로)
# - 균형잡힌 트리로 만들기위해서, Union-by-rank, Compresion Path 기법 2개를 사용

# 1. Union-by-Rank 기법
# - 각 트리에 대해 높이(rank)를 기억해두고, Union할 때 높이가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙임
# - 만약, 두 트리의 높이가 동일하다면 한 쪽 트리의 랭크를 하나 증가시킨 후, 남은 트리를 높이를 증가시킨 트리에 붙임

# 2. Path Compression 기법
# - Find를 실행한 노드를 루트노드의 직계 자식으로 만듦

# 이 두 개의 기법을 사용시 O(MlogN)의 시간복잡도


""" Kruskal's Algorithm """
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
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
    # 'edges': [
    #     (7, 'A', 'B'),
    #     (5, 'A', 'D'),
    #     (7, 'B', 'A'),
    #     (8, 'B', 'C'),
    #     (9, 'B', 'D'),
    #     (7, 'B', 'E'),
    #     (8, 'C', 'B'),
    #     (5, 'C', 'E'),
    #     (5, 'D', 'A'),
    #     (9, 'D', 'B'),
    #     (7, 'D', 'E'),
    #     (6, 'D', 'F'),
    #     (7, 'E', 'B'),
    #     (5, 'E', 'C'),
    #     (7, 'E', 'D'),
    #     (8, 'E', 'F'),
    #     (9, 'E', 'G'),
    #     (6, 'F', 'D'),
    #     (8, 'F', 'E'),
    #     (11, 'F', 'G'),
    #     (9, 'G', 'E'),
    #     (11, 'G', 'F')
    # ]
}

# 각 노드의 부모노드를 저장
parent = dict()
# 각 노드의 랭크값
rank = dict()

def make_set(node):
    parent[node] = node
    rank[node] = 0

def find(node):
    # path compression 기법 사용
    if parent[node] != node:
        # 부모노드로 올라가면서, 부모노드가 루트노드가 아니면, 이 부모노드를 루트노드의 자식노드로 만듦
        parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    # 각 노드의 루트노드를 저장
    root_u = find(u)
    root_v = find(v)

    # Union-by-rank 기법
    # 만약, u의 루트노드의 랭크가 v의 루트노드의 랭크보다 크다면,
    if rank[root_u] > rank[root_v]:
        # v의 루트노드의 부모를 u의 루트노드로 만든다.
        parent[root_v] = root_u
    # u의 루트노드의 랭크가 v의 루트노드의 랭크보다 작거나 같다면,
    else:
        parent[root_u] = root_v
        # 만약, 랭크가 같다면, 한쪽 트리의 랭크를 1 높여줌
        if rank[root_u] == rank[root_v]:
            rank[root_v] += 1

def kruskal(graph):
    # 반환할 최소 가중치를 갖는 신장트리
    mst = []

    # 먼저, Union-Find를 위해 각 노드를 부분집합으로 만든다.
    for node in graph['vertices']:
        make_set(node)

    edges = graph['edges']
    # 간선을 가중치의 오름차순으로 정렬
    edges.sort()

    # 간선을 하나씩 꺼냄
    for edge in edges:
        # 간선의 가중치와 양 노드 u,v를 저장
        weight, u, v = edge
        
        # 두 노드의 루트노드가 다르다면, 서로 다른 집합(트리)이므로 합치면 됨
        # find(): 루트노드 찾기
        if find(u) != find(v):
            # 루트노드가 다르니까 합치기
            union(u, v)
            # 합쳤으면, 이제 최소신장트리에 등록
            mst.append(edge)
            
    return mst

print(kruskal(graph))