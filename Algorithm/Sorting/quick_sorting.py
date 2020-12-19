def quick_sort(lt: list, left: int, right: int):
    if left < right:
        pivot = lt[left]
        low = left
        high = right

        while low < high:
            while lt[low] <= pivot and low <= right:
                if low == right:
                    break
                low += 1
            while pivot <= lt[high] and high >= left:
                if high == left:
                    break
                high -= 1
            if low <= high:
                lt[low], lt[high] = lt[high], lt[low]

        lt[left], lt[high] = lt[high], lt[left]    
        
        new_pivot = high

        quick_sort(lt, left, new_pivot-1)
        quick_sort(lt, new_pivot+1, right)

import random as r

# cnt = 0
# while cnt<20:
#     lt = r.sample(range(50), 30)
#     print(lt)
#     quick_sort(lt, 0, len(lt)-1)
#     print(lt)
#     cnt+=1

lt = [3, 3, 2, 2, 1, 1]
quick_sort(lt, 0, len(lt)-1)
print(lt)