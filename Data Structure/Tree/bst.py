# 이진탐색트리

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, value):
        self.cur_node = self.root

        if self.cur_node==None:
            self.root = Node(value)
            return

        while True:
            if value < self.cur_node.value:
                if self.cur_node.left != None:
                    self.cur_node = self.cur_node.left
                else:
                    self.cur_node.left = Node(value)
                    break
            # 크거나 같은 경우
            else: 
                if self.cur_node.right != None:
                    self.cur_node = self.cur_node.right
                else:
                    self.cur_node.right = Node(value)
                    break

    def search(self, value)->bool:
        self.cur_node = self.root
        while self.cur_node:
            if self.cur_node.value==value:
                return True
            elif value < self.cur_node.value:
                self.cur_node = self.cur_node.left
            else:
                self.cur_node = self.cur_node.right
        return False

    def delete(self, value)->bool:
        """
        0. 먼저 value가 있는지 확인, 없으면 리턴, 있으면 1번으로
        1. leaf node를 삭제할때
        2. 자식노드가 하나인 노드를 삭제할때
        3. 자식노드가 2개인 노드를 삭제할때 (둘 중 하나)
        (1) 삭제할노드의 오른쪽 자식의 가장 왼쪽에 있는 노드 찾기
        (2) 찾은 노드를 삭제할 노드의 위치로 이동
        (3) 해당 노드의 왼쪽/오른쪽자식을 삭제한 노드의 왼쪽/오른쪽 자식노드로 변경
        (4) 만약, 해당 노드의 오른쪽 자식이 있었다면, 이 자식노드를 해당 노드의 부모의 왼쪽 자식노드로 함
        """
        searched = False
        self.cur_node = self.root
        self.parent = self.root

        ## 먼저, 해당 값이 있는지 확인
        while self.cur_node:
            if self.cur_node.value == value:
                searched = True
                break
            elif value < self.cur_node.value:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.left
            else:
                self.parent = self.cur_node
                self.cur_node = self.cur_node.right
            
        ## 해당 값이 있으면, 삭제 알고리즘 진행
        if searched == False:
            return False

        ## 여기까지 왔으면, cur_node가 삭제할 노드이고,
        ## parent_node가 cur_node의 부모노드

        ## 1. cur_node가 말단노드일때
        if self.cur_node.left == None and self.cur_node.right == None:
            ## (1) cur_node가 parent_node의 왼쪽 자식노드일때
            if value < self.parent.value:
                self.parent.left = None
            ## (2) cur_node가 parent_node의 오른쪽 자식노드일때
            else:
                self.parent.right = None

        ## 2. cur_node의 자식노드가 하나일때
        ## (1) cur_node의 자식노드가 왼쪽에만 있을때
        if self.cur_node.left != None and self.cur_node.right == None:
            ## {1} cur_node가 parent_node의 왼쪽 노드일때
            if value < self.parent.value:
                self.parent.left = self.cur_node.left
            ## {2} cur_node가 parent_node의 오른쪽 노드일때
            else:
                self.parent.right = self.cur_node.left

        ## (2) cur_node의 자식노드가 오른쪽에만 있을때
        elif self.cur_node.left == None and self.cur_node.right != None:
            ## {1} cur_node가 parent_node의 왼쪽 노드일때
            if value < self.parent.value:
                self.parent.left = self.cur_node.right
            ## {2} cur_node가 parent_node의 오른쪽 노드일때
            else:
                self.parent.right = self.cur_node.right

        ## 3. cur_node가 자식노드를 2개 가지고 있을때
        if self.cur_node.left != None and self.cur_node.right != None:
            ## (1). cur_node가 parent_node의 왼쪽 자식노드 일때
            if value < self.parent.value:
                ## cur_node의 오른쪽 자식노드들 중에서 가장 작은 값을 찾자
                self.change_parent_node = self.cur_node.right
                self.change_node = self.cur_node.right
                while self.change_node.left:
                    self.change_parent_node = self.change_node
                    self.change_node = self.change_node.left
                ## while을 탈출하면 change_node가 가장 작은 값을 가진 노드가 된다.
                ## {1}. change_node가 오른쪽 자식노드가 있다면
                if self.change_node.right:
                    self.change_parent_node.left = self.change_node.right
                ## {2}. change_node가 오른쪽 자식노드가 없다면
                else:
                    self.change_parent_node.left = None
                ## 여기까지 오면 이제 change_node를 cur_node의 위치로 옮긴다.
                self.parent.left = self.change_node
                ## 그 후, change_node의 left, right를 연결해준다.
                self.change_node.left = self.cur_node.left
                self.change_node.right = self.cur_node.right

            ## (2). cur_node가 parent_node의 오른쪽 자식노드 일때
            elif value > self.parent.value:
                ## cur_node의 오른쪽 자식노드들 중에서 가장 작은 값을 찾자
                self.change_parent_node = self.cur_node.right
                self.change_node = self.cur_node.right
                while self.change_node.left:
                    self.change_parent_node = self.change_node
                    self.change_node = self.change_node.left
                ## while을 탈출하면 change_node가 가장 작은 값을 가진 노드가 된다.
                ## {1}. change_node가 오른쪽 자식노드가 있다면
                if self.change_node.right:
                    self.change_parent_node.left = self.change_node.right
                ## {2}. change_node가 오른쪽 자식노드가 없다면
                else:
                    self.change_parent_node.left = None
                ## 여기까지 오면 이제 change_node를 cur_node의 위치로 옮긴다.
                self.parent.right = self.change_node
                ## 그 후, change_node의 left, right를 연결해준다.
                self.change_node.left = self.cur_node.left
                self.change_node.right = self.cur_node.right

        del self.cur_node
        return True

    ## preorder traversal
    def traversal(self, root):
        cur_node = root
        if cur_node == None:
            return
        self.traversal(cur_node.left)
        print(cur_node.value, end=' ')
        self.traversal(cur_node.right)


print()
bst = BST()
bst.insert(50)
bst.insert(28)
bst.insert(80)
bst.insert(17)
bst.insert(41)
bst.insert(31)
bst.insert(66)
bst.insert(90)
bst.insert(72)

bst.traversal(bst.root)