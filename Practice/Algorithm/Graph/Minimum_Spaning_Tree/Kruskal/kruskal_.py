# Spanning Tree
# - 원래 그래프의 모든 노드가 연결되어 있으면서 트리의 속성을 만족하는 그래프

# Spanning Tree의 조건
# - 모든 노드가 서로 연결
# - 사이클이 존재하지 않음
# - 원래 그래프의 모든 노드를 포함해야함

# Minimum Spanning Tree
# - Spanning Tree 중에서, 간선의 가중치 합이 최소인 Spanning Tree

# Minimum Spanning Tree의 구현
# - Kruskal's Algorithm 
# - Prim's Algorithm
# - 간선의 수가 작으면 크루스칼, 많으면 프림 알고리즘 사용

# Union-Find Algorithm
# - Disjoint Set을 나타내기 위한 알고리즘
# - Disjoint Set이란, 서로소 집합 자료구조
# - 트리를 이용하면, 루트노드로 서로 같은 집합인지 확인할 수 있으며, 하나의 트리가 하나의 집합을 뜻함
# - make-set, union, find ADT를 제공
# - make-set(n) : n개의 노드들을 각각 서로소 집합으로 만드는 연산
# - union(a,b) : 두 개별 집합(a,b)을 하나의 집합으로 합치는 연산
# - find(a) : 인자로 받은 개별 집합(a)의 루트노드를 반환하는 연산(루트노드가 같으면, 같은 집합에 속한 것)

# Kruskal's Algorithm의 구현
# - Union-Find Algorithm을 이용하여, 두 집합(트리)를 연결했을때, 사이클 유무를 판단함

# 크루스칼 알고리즘의 시간복잡도
# - O(ElogE)

parents = {}
ranks = {}
def make_set(vertex):
    parents[vertex] = vertex
    ranks[vertex] = 0
def find(vertex):
    if parents[vertex] != vertex:
        parents[vertex] = find(parents[vertex])
    return parents[vertex]
def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if root1 == root2:
        return False
    if ranks[root1] > ranks[root2]:
        parents[root2] = root1
    elif ranks[root1] < ranks[root2]:
        parents[root1] = root2
    else:
        ranks[root1] += 1
        parents[root2] = root1
    return True
def kruskal(graph):
    mst = []
    # 1. 최초에 모든 정점들을 독립적인 집합으로 만듦 - O(V)
    for vertex in graph['vertices']:
        make_set(vertex)
    # 2. 모든 간선들을 정렬 - O(Elog(E))
    edges = graph['edges']
    edges.sort()
    # 3. 간선들을 돌면서 정점들을 연결 (단, 사이클이 생기면 넘어가기) - O(logE)
    for edge in edges:
        w, u, v = edge
        if union(u, v):
            mst.append(edge)
    return mst
g = {
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
}
print(kruskal(g))