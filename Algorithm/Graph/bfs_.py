# BFS는 큐 2개로 구현
# 시간복잡도 = O(V+E), print로 확인해보기

def BFS(graph, root):
    # 방문한 노드들을 기록
    visited = []
    # 방문해야 할 노드들을 기록
    need_visit = []

    need_visit.append(root)

    # need_visit이 비어있다면, 모든 노드를 방문한 것이므로 while문 탈출
    # [파이썬에서는 리스트(멤버쉽)의 크기가 0이 아니면 while문 True, 0이면 False]
    while need_visit:
        node = need_visit.pop(0)
        # 만약, visited 안에 node가 없다면,
        if node not in visited:
            # visited에다가
            visited.append(node)
            # list의 매소드 append는 단일 원소를 붙이는 것, extend는 리스트를 붙이는 것
            need_visit.extend(graph[node])
        
    return visited

graph = dict()

# value는 리스트형태
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

graph2 = dict()
graph2['A'] = ['B','C','E']
graph2['B'] = ['A','C']
graph2['C'] = ['A','B','D','E']
graph2['D'] = ['C','E']
graph2['E'] = ['A','C','D']

print(BFS(graph2, 'A'))