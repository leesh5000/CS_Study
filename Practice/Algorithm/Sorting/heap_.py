# Heap Sort
# - 힙 자료구조의 특징을 이용한 정렬
# - O(nlogn) = n * O(logn) (힙의 데이터 저장의 시간복잡도)

class heap:
    def __init__(self):
        self.lt = []
    def push(self, item):
        self.lt.append(item)
        cur_idx = len(self.lt)-1
        while cur_idx != 0:
            parent_idx = (cur_idx-1)//2
            if self.lt[cur_idx] <= self.lt[parent_idx]:
                self.lt[cur_idx], self.lt[parent_idx] = self.lt[parent_idx], self.lt[cur_idx]
                cur_idx = parent_idx
            else:
                break
    def pop(self):
        if len(self.lt) == 0:
            return
        if len(self.lt) == 1:
            return self.lt.pop()
        ret_item = self.lt[0]
        self.lt[0] = self.lt.pop()
        cur_idx = 0
        while True:
            left_child_idx = (cur_idx+1)*2-1
            right_child_idx = (cur_idx+1)*2
            last_idx = len(self.lt)-1
            # 자식노드가 없는 경우
            if left_child_idx > last_idx:
                break
            # 자식노드가 하나만 있는 경우는, 왼쪽 자식이랑만 비교하면 된다.
            elif left_child_idx == last_idx:
                if self.lt[left_child_idx] <= self.lt[cur_idx]:
                    self.lt[left_child_idx], self.lt[cur_idx] = self.lt[cur_idx], self.lt[left_child_idx]
                    cur_idx = left_child_idx
                else:
                    break
            # 자식노드가 둘 다 있는 경우는 두 자식노드 중 더 우선순위가 높은 자식노드랑 비교해야한다.
            else:
                # 왼쪽 자식노드가 오른쪽 자식노드보다 우선순위가 더 높고,
                if self.lt[left_child_idx] < self.lt[right_child_idx]:
                    # 왼쪽자식노드가 현재노드보다 우선순위가 더 높으면 스왑하기
                    if self.lt[left_child_idx] <= self.lt[cur_idx]:
                        self.lt[left_child_idx], self.lt[cur_idx] = self.lt[cur_idx], self.lt[left_child_idx]
                        cur_idx = left_child_idx
                    # 왼쪽자식노드가 오른쪽자식노드보다는 우선순위가 높은데, 현재노드보다는 우선순위가 더 낮다면 그냥 끝내기
                    else:
                        break
                # 오른쪽 자식노드가 왼쪽 자식노드보다 우선순위가 더 높다면,
                else:
                    # 오른쪽자식노드가 현재노드보다 우선순위가 더 높으면 스왑하기
                    if self.lt[right_child_idx] <= self.lt[cur_idx]:
                        self.lt[right_child_idx], self.lt[cur_idx] = self.lt[cur_idx], self.lt[right_child_idx]
                        cur_idx = right_child_idx
                    # 왼쪽자식노드가 오른쪽자식노드보다는 우선순위가 높은데, 현재노드보다는 우선순위가 더 낮다면 그냥 끝내기
                    else:
                        break
        return ret_item
                    

def test(n):
    import random as r
    cnt = 0
    while cnt < n:
        lt = [r.randrange(100) for i in range(50)]
        print('original :', lt)
        h = heap()
        sorted_lt = []
        for i in range(len(lt)):
            h.push(lt[i])
        while len(h.lt) != 0:
            sorted_lt.append(h.pop())
        for i in range(len(sorted_lt)-1):
            if sorted_lt[i] > sorted_lt[i+1]:
                return print('sorting failed :', sorted_lt)
        print('sorted :', sorted_lt)
        cnt+=1
    return print('sorting success')

test(100)