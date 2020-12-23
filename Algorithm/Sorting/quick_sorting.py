# def quick_sort(lt: list, left: int, right: int):
#     if left < right:
#         pivot = lt[left]
#         low = left
#         high = right

#         while low < high:
#             while lt[low] <= pivot and low <= right-1:
#                 low += 1
#             while pivot <= lt[high] and high >= left+1:
#                 high -= 1
#             if low <= high:
#                 lt[low], lt[high] = lt[high], lt[low]

#         lt[left], lt[high] = lt[high], lt[left]    
        
#         new_pivot = high

#         quick_sort(lt, left, new_pivot-1)
#         quick_sort(lt, new_pivot+1, right)

# def quick_sort2(lt: list):
#     if len(lt) <= 1:
#         return lt
    
#     pivot = lt[0]

#     left = [i for i in lt[1:] if pivot > i]
#     right = [i for i in lt[1:] if pivot <= i]

#     return quick_sort2(left) + [pivot] + quick_sort2(right)



# -------------------------------------------------------------

import random as r

lt = [3, 3, 3, 2, 2, 1, 1,2,4,1,6,5]
lt2 = [3, 2, 4, 7, 5, 6]
# quick_sort(lt, 0, len(lt)-1)
print(quick_sort2(lt))

# cnt = 0
# while cnt<1000:
#     lt = r.sample(range(100000), 1000)
#     quick_sort(lt, 0, len(lt)-1)
#     for i in range(len(lt)-1):
#         if lt[i]>lt[i+1]:
#             print(False)
#     cnt+=1