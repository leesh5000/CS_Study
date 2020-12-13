class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def append(self, data):
        """
        append : 리스트 맨 끝에 노드 추가하는 함수
        1. head가 빈 경우 -> head에 추가
        """
        cur_node = self.head
        if cur_node == None:
            self.head = Node(data)
            return
        # 아래처럼 하면 안된다.
        # cur_node는 스택영역이므로 함수가 종료되면서 소멸되기때문에
        # while cur_node:
        #     cur_node = cur_node.next
        # cur_node = Node(data)
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = Node(data)
    def Insert(self, data, target_data):
        """
        세가지 경우
        1.연결리스트에 아무 노드도 없는 경우 -> 함수끝내기
        2.target_data를 찾지못한 경우 -> 함수끝내기
        3.target_data를 찾은경우 -> target 뒤에 노드 추가
        """
        new_node = Node(data)
        cur_node = self.head
        # 노드에 아무것도 없다면, 헤드에 노드 추가
        if cur_node==None:
            print("\nempty list")
            return
        # target_data 찾기
        while cur_node.data!=target_data:
            cur_node = cur_node.next
            # 타겟을 못 찾았으면 함수 끝내기
            if cur_node==None:
                print("\nnot found data")
                return
        tmp_node = cur_node.next
        cur_node.next = new_node
        new_node.next = tmp_node
    def delete(self, target_data):
        """
        1.헤드가 없는 경우 -> 함수 끝내기
        2.target_data가 존재하는경우 -> 해당 데이터 삭제하기
            (1).target_data가 헤드인 경우
        """
        cur_node = self.head
        if cur_node==None:
            print("\nempty list")
            return
        
        if cur_node.data == target_data:
            tmp_node = self.head
            self.head = self.head.next
            del tmp_node
            return 

        while cur_node.next:
            if cur_node.next.data == target_data:
                tmp_node = cur_node.next
                cur_node.next = tmp_node.next
                del tmp_node
                return
            cur_node = cur_node.next
        print("\nnot found data")
    def traversal(self):
        node = self.head
        print('\n')
        while node:
            print(node.data)
            node = node.next

ll = LinkedList()

for i in range(10):
    ll.append(i)

ll.Insert(100, 0)
ll.Insert(99, -1)
ll.traversal()

ll.delete(0)
ll.delete(6)
ll.delete(99)
ll.traversal()
print(ll.head.data)