# Selection Sort
# 시간복잡도 O(N^2)

def selection_sort(lt):
    for i in range(len(lt)-1):
        # 최소값을 가지는 인덱스
        min_idx = i
        for j in range(i+1, len(lt)):
            if lt[j] < lt[min_idx]:
                min_idx = j
        if lt[i] > lt[min_idx]:
            lt[i], lt[min_idx] = lt[min_idx], lt[i]

def test(n):
    import random as r
    cnt = 0
    while cnt < n:
        lt = r.sample(range(100), 30)
        print('original :', lt)
        selection_sort(lt)
        for i in range(len(lt)-1):
            if lt[i] > lt[i+1]:
                return print('sorting failed :', lt)
        print('sorted :', lt)
        cnt+=1
    return print('sorting success')

test(1000)

                

