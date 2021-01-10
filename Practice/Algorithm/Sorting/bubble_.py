# Bubble Sort
# - O(n^2)의 시간복잡도

def bubble_sort(lt):
    for i in range(len(lt)-1):
        swap = False
        for j in range(len(lt)-1-i):
            if lt[j] > lt[j+1]:
                lt[j], lt[j+1] = lt[j+1], lt[j]
                swap = True
        if swap == False:
            break

import random as r

lt = r.sample(range(10000), 20)
print('not sorted :',lt)
bubble_sort(lt)
print('sorted :',lt)