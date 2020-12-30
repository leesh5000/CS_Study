# Tree
# - Node와 Branch로 사이클을 이루지 않는 자료구조
# - 데이터를 표현하는데 초점을 둔 자료구조
# - 그래프의 스페셜 케이스
# - 여러 종류의 변형이 있음
# - 트리의 높이를 구하는 문제
# - 트리의 BFS는 Level Order Search, DFS는 Pre/In/Postorder Traverse

# 배열을 이용하여 구현

# 트리의 노드를 표현한 클래스
class node:
    def __init__(self, data):
        self.data = data
        self.children = []

class tree:
    # 트리 생성자
    def __init__(self):
        self.root = None
    # 트리 출력 함수
    def print_tree(self, root):
        print(root.data)
        for child in root.children:
            self.print_tree(child)
    # 트리의 높이 반환하는 함수
    def get_height(self, root)->int:
        height = 0
        for child in root.children:
            height = max(height, self.get_height(child) + 1)
        
        return height

r = node('컴퓨터공학')
t = tree()
t.root = r
n = node('컴퓨터구조')
n.children.append(node('기계어'))
n.children.append(node('파이프라인'))
n.children.append(node('가상메모리'))
t.root.children.append(n)
v = node('운영체제')
v.children.append(node('프로세스'))
v.children.append(node('스레드'))
t.root.children.append(v)
m = node('네트워크')
m.children.append(node('응용계층'))
m.children.append(node('전송계층'))
m.children.append(node('네트워크계층'))
t.root.children.append(m)

t.print_tree(r)
print(t.get_height(r))