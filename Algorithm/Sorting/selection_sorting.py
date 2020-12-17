def selection_sorting(lt) -> list:
    for i in range(len(lt)-1):
        min_idx = i
        for j in range(i, len(lt)):
            if lt[min_idx] > lt[j]:
                min_idx = j
        lt[i], lt[min_idx] = lt[min_idx], lt[i]
    return lt

import random as r

lt = r.sample(range(30),15)
print(selection_sorting(lt))