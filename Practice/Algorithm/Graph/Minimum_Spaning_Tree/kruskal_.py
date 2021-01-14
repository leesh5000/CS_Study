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

""" Union-Find Algorithm """
class disjoint_set:
    def __init__(self):
        # 각 노드의 부모노드 정보가 담긴 딕셔너리
        self.parents = dict()
        # 현재 노드(원소)들을 담는 집합
        self.items = set()
        self.rank = dict()
    # item을 갖는 집합을 만드는 함수
    def make_set(self, item):
        # 현재 원소들을 담는 집합에 먼저 item을 넣고
        self.items.add(item)
        # 최초에 item노드의 부모노드는 자기자신임
        self.parents[item] = item
        # 최초에 rank는 0
        self.rank[item] = 0
    # 인자로 받은 item의 루트노드를 반환
    def find(self, item):
        """ 최적화 find 연산 - path compression 사용 """
        if self.parents[item] != item:
            self.parents[item] = self.find(self.parents[item])
            return self.parents[item]
        else:
            return self.parents[item]
        """ 기본 find 연산 """
        # # 자신의 부모가 자기자신이면, 루트노드라는 뜻
        # if self.parents[item] == item:
        #     return item
        # # 그게아니라면, 한번더 find를 해서 재귀적으로 부모를 찾기
        # else:
        #     return self.find(self.parents[item])

    # 인자로 받은 두 집합을 합치는 연산, 같은집합(루트노드가 같으면)이면 false
    def union(self, item1, item2):
        """ 최적화 union 연산 - union by rank 사용 """
        # 먼저 item1, item2의 루트노드를 찾는다.
        root1 = self.find(item1)
        root2 = self.find(item2)
        print(root1, root2)
        # 만약, root1 랭크가 root2 랭크보다 더 높다면, 랭크가 더 작은쪽을 더 큰 쪽에 붙여주기
        if self.rank[root1] > self.rank[root2]:
            self.parents[root2] = root1
        # 오른쪽이 더 랭크가 크다면,
        elif self.rank[root1] < self.rank[root2]:
            self.parents[root1] = root2
        # 두 랭크가 같다면, 한 쪽 랭크를 1 증가시키고 붙이기
        else:
            self.rank[root1] += 1
            self.parents[root2] = root1            
        """ 기본 union 연산 """
        # if self.find(item1) == self.find(item2):
        #     print('violated disjoint set')
        #     return False
        # else:
        #     self.parents[item2] = item1
        
s = disjoint_set()
s.make_set('A')
s.make_set('B')
s.make_set('C')
s.make_set('D')
print(s.parents, s.items)
s.union('A','B')
s.union('A','C')
print(s.parents, s.items)
s.union('B', 'D')
print(s.parents, s.items)
