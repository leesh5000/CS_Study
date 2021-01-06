# Merge Sorting
# O(nlogn)
# 동적계획 분할정복 중 분할정복 기법
# 동적계획
# - 문제를 작게 나누어 작은 문제부터 풀고 이 해를 이용하여 더 큰 문제를 풀어나가는 방법
# - 상향식 접근법
# - 메모이제이션 사용
# 분할정복
# - 그대로 해결할 수 없는 문제를 작은 문제로 분할하여 문제를 해결하는 방법
# - 하향식 접근법
# - 재귀용법 사용

def merge_sort(lt, start, end):
    if start < end:
        mid = int((start+end) / 2)
        # 분할과정
        merge_sort(lt, start, mid)
        merge_sort(lt, mid+1, end)

        ## Merge
        left = start
        right = mid+1
        temp = []

        # 만약, left가 mid보다 작고, right도 end보다 작은 상태에서
        while left <= mid and right <= end:
            if lt[left] <= lt[right]:
                temp.append(lt[left])
                left += 1
            else:
                temp.append(lt[right])
                right += 1
        
        # left > mid 라는것은 아직 right 쪽에 남은 값들이 있다는 것, =는 안나온다.
        if left > mid:
            for i in range(right, end+1):
                temp.append(lt[i])
        else:
            for i in range(left, mid+1):
                temp.append(lt[i])

        idx = 0
        for i in range(start, end+1):
            lt[i] = temp[idx]
            idx += 1

import random
lt = random.sample(range(1000), 30)
merge_sort(lt, 0, len(lt)-1)
print(lt)

            

