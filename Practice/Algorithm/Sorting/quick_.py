# Quick Sorting
# O(nlog(n))

# def quick_sort(lt, left, right):
#     if left < right:
#         pivot = lt[left]
#         low = left
#         high = right

#         while low < high:
#             while pivot >= lt[low] and low != right:
#                 low += 1
#             while pivot <= lt[high] and high != left:
#                 high -= 1
#             if low <= high:
#                 lt[low], lt[high] = lt[high], lt[low]
        
#         lt[left], lt[high] = lt[high], lt[left]

#         quick_sort(lt, left, high-1)
#         quick_sort(lt, high+1, right)

def quick_sort(lt, left, right):
    if left < right:
        pivot = lt[left]
        low = left
        high = right

        while low < high:
            while pivot >= lt[low] and low != right:
                low += 1
            while pivot <= lt[high] and high != left:
                high -= 1
            if low <= high:
                lt[low], lt[high] = lt[high], lt[low]
        
        lt[left], lt[high] = lt[high], lt[left]

        quick_sort(lt, left, high-1)
        quick_sort(lt, high+1, right)

def quick_sort_pythonic(lt):
    if len(lt) == 1:
        return lt
    
    pivot = lt[0]
    left = [i for i in lt[1:] if pivot > i]
    right = [i for i in lt[1:] if pivot <= i]

    return quick_sort_pythonic(left) + [pivot] + quick_sort_pythonic(right)

import random

lt = random.sample(range(1000), 30)
quick_sort(lt, 0, len(lt)-1)
print(lt)