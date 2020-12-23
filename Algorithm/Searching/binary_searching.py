# 분할정복과 이진탐색

def bin_search(lt: list, target: int)->bool:
    # 리스트가 하나 남았다면,
    print(lt)
    if len(lt)<=1:
        if lt[0] == target:
            return True
        if lt[0] != target:
            return False
    
    mid = int(len(lt)/2)

    if lt[mid] == target:
        return True
    elif lt[mid] > target:
        return bin_search(lt[:mid], target)
    elif lt[mid] < target:
        return bin_search(lt[mid+1:], target)

lt = [1, 2, 3, 4, 9, 11, 100, 2910]
lt.sort()
print(bin_search(lt, 2))

# import random as r

# cnt = 0
# while cnt != 1000:
#     lt = r.sample(range(10000), 100)
#     rand_idx = r.randint(0, 99)
#     lt.sort()
#     print(bin_search(lt, lt[rand_idx]))
#     cnt+=1
