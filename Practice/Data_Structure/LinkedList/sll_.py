# 연결리스트
# - 포인터만 연결하면 되므로 데이터의 삽입/삭제에 O(1) 시간복잡도를 갖는다.
# - 맨 앞의 노드 혹은 맨 뒤의 노드에서 출발해야하므로 데이터의 조회에 O(n)의 시간복잡도를 갖는다.
# - 다른 여러 자료구조의 기반이 된다.

class sll:
    class node:
        def __init__(self, data):
            self.next = None
            self.data = data

    def __init__(self):
        self.head = None

    # 매개변수 data를 연결리스트 끝에 추가하는 함수
    def append(self, data):
        if self.head == None:
            self.head = self.node(data)
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = self.node(data)

    # 매개변수 data와 같은 값을 가진 노드를 삭제하는 함수
    def delete(self, data):
        cur_node = self.head
        
        # 만약, head가 data와 같다면,
        if cur_node.data == data:
            tmp_node = cur_node
            self.head = cur_node.next
            del tmp_node
            return
        
        # 그게 아니라면,
        while cur_node.next:
            if cur_node.next.data == data:
                tmp_node = cur_node.next
                cur_node.next = cur_node.next.next
                del tmp_node
                return
            else:
                cur_node = cur_node.next

        # 여기까지 오면, data와 같은 노드를 못 찾았으므로 리턴
        print('not found')
        return False

    def print(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

ll = sll()
ll.append(10)
ll.append(5)
ll.append(1)
ll.append(7)
ll.delete(5)
ll.print()
print(ll.head.data)

        