def merge_sort(lt: list, start: int, end: int):
    if start < end:
        mid = (start + end) // 2
        merge_sort(lt, start, mid)
        merge_sort(lt, mid+1, end)

        ## Merge
        left_idx = start
        right_idx = mid+1
        sort_lt = []

        while left_idx <= mid and right_idx <= end:
            if lt[left_idx] <= lt[right_idx]:
                sort_lt.append(lt[left_idx])
                left_idx += 1
            else:
                sort_lt.append(lt[right_idx])
                right_idx += 1

        if left_idx > mid:
            for i in range(right_idx, end+1):
                sort_lt.append(lt[i])
        else:
            for i in range(left_idx, mid+1):
                sort_lt.append(lt[i])

        sort_idx = 0
        for i in range(start, end+1):
            lt[i] = sort_lt[sort_idx]
            sort_idx += 1

def merge_sort2(lt: list):
    if len(lt) <= 1:
        return lt
    mid = int(len(lt)/2)
    left = merge_sort2(lt[:mid])
    right = merge_sort2(lt[mid:])

    sorted_lt = list()
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            sorted_lt.append(right[right_idx])
            right_idx += 1
        else:
            sorted_lt.append(left[left_idx])
            left_idx += 1
        
    while left_idx < len(left):
        sorted_lt.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        sorted_lt.append(right[right_idx])
        right_idx += 1

    return sorted_lt
    

import random as r

cnt = 0
while cnt < 10000:
    lt = r.sample(range(100000), 1000)
    # merge_sort(lt, 0, len(lt)-1)
    sorted_lt = merge_sort2(lt)
    for i in range(0, len(lt)-1):
        if sorted_lt[i] > sorted_lt[i+1]:
            print("Sort Failed!")
        # else:
        #     print(sorted_lt[i])
        cnt += 1
