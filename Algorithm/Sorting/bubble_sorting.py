def bubble_sort(lt):
    for i in range(len(lt)-1):
        for j in range(len(lt)-1):
            if lt[j] > lt[j+1]:
                lt[j], lt[j+1] = lt[j+1], lt[j]
    return lt

import random as r

lt = r.sample(range(100), 100)
print(bubble_sort(lt))
