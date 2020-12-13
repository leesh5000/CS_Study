class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DLinkedList:
    def __init__(self, head=None, tail=None):
        self.tail = tail
        self.head = head
    def append(self, data):
        cur_node = self.head
        if cur_node == None:
            self.head = Node(data)
            self.tail = self.head
            return
        
        new_node = Node(data)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node      
    def insert_after(self, data, target_data):
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
        new_node.prev = cur_node
        new_node.next.prev = new_node
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
        
        if self.head.data == target_data:
            tmp_node = self.head
            self.head = self.head.next
            del tmp_node
            return 

        while cur_node.next:
            if cur_node.next.data == target_data:
                tmp_node = cur_node.next
                cur_node.next = tmp_node.next
                tmp_node.prev = cur_node
                del tmp_node
                if cur_node.next.next == None:
                    self.tail = cur_node.next 
                return
            cur_node = cur_node.next
        print("\nnot found data")
    def traversal(self):
        node = self.head
        print('\n')
        while node:
            print(node.data)
            node = node.next
    def search_from_head(self, data)->Node:
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                return cur_node
            else:
                cur_node = cur_node.next

        print('not found node')
        return False
    def search_from_tail(self, data)->Node:
        cur_node = self.tail
        while cur_node:
            if cur_node.data == data:
                return cur_node
            else:
                cur_node = cur_node.prev

        print('not found node')
        return False
    def insert_before(self, data, target_data):
        """
        세가지 경우
        1.연결리스트에 아무 노드도 없는 경우 -> 함수끝내기
        2.target_data를 찾지못한 경우 -> 함수끝내기
        3.target_data를 찾은경우 -> target 뒤에 노드 추가
        """
        new_node = Node(data)
        cur_node = self.head

        # target_data 찾기
        while cur_node:
            if cur_node.data == target_data:
                if cur_node.prev == None:
                    cur_node.prev = new_node
                    new_node.next = cur_node
                    self.head = new_node
                    return
                tmp_node = cur_node.prev
                cur_node.prev = new_node
                new_node.next = cur_node
                new_node.prev = tmp_node
                tmp_node.next = new_node
                return
            else:
                cur_node = cur_node.next

        print('not found data')
        return


ll = DLinkedList()

for i in range(10):
    ll.append(i)

ll.insert_after(100, 0)
ll.insert_after(99, -1)
ll.traversal()

ll.delete(0)
ll.delete(6)
ll.delete(99)
ll.traversal()
print(ll.head.data)
print(ll.tail.data)

print(ll.search_from_head(4).data)
print(ll.search_from_head(100).data)
print(ll.search_from_tail(100).data)

ll.insert_before(-1, 100)
ll.insert_before(77,7)
ll.traversal()