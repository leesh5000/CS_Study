def insertion_sort(lt)->list:
    for i in range(len(lt)):
        ins_idx = i
        for j in range(i, 0, -1):
            if lt[ins_idx] < lt[j-1]:
                lt[ins_idx], lt[j-1] = lt[j-1], lt[ins_idx]
                ins_idx = j-1
            else:
                break
    return lt

import random as r

lt = [5,3,2,4,1]
print(insertion_sort(lt))