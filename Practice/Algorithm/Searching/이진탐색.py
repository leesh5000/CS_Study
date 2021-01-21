def binary_search_recur(lt, start, end, target):
    mid = (start + end)//2
    if start > end:
        return False
    if target == lt[mid]:
        return mid
    if target > lt[mid]:
        return binary_search_recur(lt, mid+1, end, target)
    else:
        return binary_search_recur(lt, start, mid-1, target)

def binary_search(lt, target):
    left = 0
    right = len(lt)-1
    while left <= right:
        mid = (left+right)//2
        if lt[mid] == target:
            return mid
        elif lt[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

import random
lt = []
for i in range(30):
    lt.append(random.randrange(0, 30))
lt = list(sorted(lt))
print(lt)
print(binary_search_recur(lt, 0, len(lt)-1, 5))
print(binary_search(lt, 5))