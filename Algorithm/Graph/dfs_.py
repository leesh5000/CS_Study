# BFS는 큐 1개, 스택 1개로 구현
# 시간복잡도 = O(V+E), print로 확인해보기

def DFS(graph, root):
    # 방문한 노드를 기록 (큐로 사용)
    visited = []
    # 방문할 노드를 기록 (스택으로 사용)
    need_visit = []
    need_visit.append(root)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
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

print(DFS(graph,'A'))