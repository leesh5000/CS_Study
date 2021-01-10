# 그래프
# - 정점과 정점들을 잇는 간선들로 이루어진 자료구조
# - 트리는 노드간의 부모관계가 있고, 사이클을 이루지 않고, 방향성이 있는 그래프

# 그래프의 구현
# - 인접리스트 이용
# ex) a[1] : 2,3,4 // a[2] : 1,4 // a[3] : 1,4 // a[4] : 1,2,3
# - 인접행렬 이용
# ex) a[1][2], a[1][3], a[1][4] = 1 / a[2][1], a[2][4] = 1 / a[3][1], a[3][4] = 1 / a[4][1], a[4][2], a[4][3] = 1

# dfs
# - 한 

def bfs(graph, start):
    visited = []
    need_visit_queue = []
    need_visit_queue.append(start)
    while need_visit_queue:
        v = need_visit_queue.pop(0)
        if v not in visited:
            need_visit_queue.extend(graph[v])
            print(v)
            visited.append(v)

def dfs(graph, start):
    visited = []
    need_visit_stack = []
    need_visit_stack.append(start)
    while need_visit_stack:
        v = need_visit_stack.pop()
        if v not in visited:
            graph[v].reverse()
            need_visit_stack.extend(graph[v])
            print(v)
            visited.append(v)

graph = dict()
graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']

bfs(graph, 'A')
print()
dfs(graph, 'A')