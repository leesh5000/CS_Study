class heap:
    def __init__(self):
        self.lt = []
        self.lt.append(None)
    def push(self, item):
        self.lt.append(item)
        cur_idx = len(self.lt)-1
        while cur_idx != 1:
            parent_idx = cur_idx // 2
            if self.lt[cur_idx] <= self.lt[parent_idx]:
                self.lt[cur_idx], self.lt[parent_idx] = self.lt[parent_idx], self.lt[cur_idx]
                cur_idx = parent_idx
            else:
                break
    def pop(self):
        if len(self.lt) == 1:
            return
        del_item = self.lt[1]
        last_idx = len(self.lt)-1
        self.lt[1] = self.lt[last_idx]
        del self.lt[last_idx]
        last_idx -= 1
        cur_idx = 1
        while True:
            left_child_idx = cur_idx * 2
            right_child_idx = cur_idx * 2 + 1
            
            # 왼쪽자식노드의 인덱스가 마지막 인덱스 크다면 빠져나오고
            if left_child_idx > last_idx:
                break
            # 왼쪽자식노드의 인덱스가 마지막 인덱스와 같다면,
            elif left_child_idx == last_idx:
                # 왼쪽자식노드랑만 비교하고 스왑하기
                if self.lt[left_child_idx] <= self.lt[cur_idx]:
                    self.lt[left_child_idx], self.lt[cur_idx] = self.lt[cur_idx], self.lt[left_child_idx]
                    cur_idx *= 2
                else:
                    break
            # 둘다 아니라면, 자식노드는 왼쪽, 오른쪽 모두 있는것이므로
            else:
                # 두 자식노드 중 더 낮은 값이랑 스왑한다.
                if self.lt[left_child_idx] <= self.lt[right_child_idx]:
                    self.lt[left_child_idx], self.lt[cur_idx] = self.lt[cur_idx], self.lt[left_child_idx]
                    cur_idx *= 2
                else:
                    self.lt[right_child_idx], self.lt[cur_idx] = self.lt[cur_idx], self.lt[right_child_idx]
                    cur_idx = cur_idx * 2 + 1
        return del_item

    def print(self):
        print(self.lt[1:])