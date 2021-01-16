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

# def merge_sort(lt, start, end):
#     if start >= end:
#         return
#     # 작은문제로 나누기
#     mid = (start + end) // 2
#     merge_sort(lt, start, mid)
#     merge_sort(lt, mid+1, end)
#     # merge
#     left = start
#     right = mid+1
#     a = []
#     while left <= mid and right <= end:
#         if lt[left] < lt[right]:
#             a.append(lt[left])
#             left += 1
#         else:
#             a.append(lt[right])
#             right += 1
#     # 여기까지 오면, left, right 중 어느하나는 mid, end를 넘었다.
#     if left > mid:
#         for i in range(right, end+1):
#             a.append(lt[i])
#     else:
#         for i in range(left, mid+1):
#             a.append(lt[i])
#     # 정렬된 리스트를 원래 리스트로 넣어주기
#     for i in range(start, end+1):
#         lt[i] = a.pop(0)

def merge_sort(lt, start, end):
    if start >= end:
        return
    mid = (start+end)//2
    merge_sort(lt, start, mid)
    merge_sort(lt, mid+1, end)
    temp = []
    left = start
    right = mid+1
    while left <= mid and right <= end:
        if lt[left] < lt[right]:
            temp.append(lt[left])
            left += 1
        else:
            temp.append(lt[right])
            right += 1
    if left > mid:
        for i in range(right, end+1):
            temp.append(lt[i])
    else:
        for i in range(left, mid+1):
            temp.append(lt[i])
    for i in range(start, end+1):
        lt[i] = temp.pop(0)

def test(n):
    import random as r
    cnt = 0
    while cnt < n:
        sample_lt = r.sample(range(100), 30)
        lt = [r.choice(sample_lt) for i in range(30)]
        print('original :', lt)
        merge_sort(lt, 0, len(lt)-1)
        for i in range(len(lt)-1):
            if lt[i] > lt[i+1]:
                return print('sorting failed :', lt)
        print('sorted :', lt)
        cnt+=1
    return print('sorting success')

test(1000)

            

