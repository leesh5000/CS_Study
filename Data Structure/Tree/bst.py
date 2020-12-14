# 이진탐색트리

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self, root):
        self.root = root
    
    def insert(self, value):
        self.cur_node = self.root

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

root = Node(10)
bst = BST(root)
bst.insert(1)
bst.insert(20)

