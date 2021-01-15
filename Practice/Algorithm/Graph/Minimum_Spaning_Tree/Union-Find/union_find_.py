# Union-Find Algorithm
# - 서로소집합 자료구조를 나타내기 위한 알고리즘
# - 각 집합을 트리로 표현
# - make-set, find, union 연산

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
print(s.parents, s.items, s.rank)

parents = dict()
ranks = dict()

def make_set(item):
    parents[item] = item
    ranks[item] = 0

def find(item):
    if parents[item] != item:
        parents[item] = find(parents[item])
        return parents[item]
    else:
        return item

def union(item1, item2):
    root1 = find(item1)
    root2 = find(item2)
    if ranks[root1] > ranks[root2]:
        parents[root2] = root1
    elif ranks[root1] < ranks[root2]:
        parents[root1] = root2
    else:
        ranks[root1] += 1
        parents[root2] = root1

make_set('A')
make_set('B')
make_set('C')
make_set('D')
make_set('E')
make_set('F')
union('A','B')
union('B','C')
print(parents)

