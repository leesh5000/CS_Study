# 트리는 계속해서 늘어날 수 있으니까 자식들을 리스트로 하는것이 좋다.
# 이진트리는 연결리스트가 좋다. (왼쪽,오른쪽뿐이니까)

class node:
    def __init__(self, data):
        self.data = data
        self.children = []

class tree:
    def __init__(self):
        self.root = None
    """ 이진트리의 bfs = pre,in,postorder / dfs = level order first. 그냥 트리는 bfs, dfs """
    def dfs(self, start):
        need_visit = []
        need_visit.append(start)
        while need_visit:
            v = need_visit.pop()      
            need_visit.extend(reversed(v.children))
            print(v.data)
    def bfs(self, start):
        need_visit = []
        need_visit.append(start)
        while need_visit:
            v = need_visit.pop(0)      
            need_visit.extend(v.children)
            print(v.data)

t = tree()
t.root = node('Computer Science')
t.root.children.append(node('Computer Architecture'))
t.root.children.append(node('Operating System'))
t.root.children.append(node('Network'))
t.root.children[0].children.append(node('ISA'))
t.root.children[0].children.append(node('Pipelining'))
t.root.children[0].children.append(node('Memory'))
t.root.children[1].children.append(node('Process Synchronization'))
t.root.children[1].children.append(node('CPU Scheduling'))
t.root.children[1].children.append(node('Memory Management'))
t.root.children[2].children.append(node('Application Layer'))
t.root.children[2].children.append(node('Transport Layer'))
t.root.children[2].children.append(node('Network Layer'))

t.dfs(t.root)