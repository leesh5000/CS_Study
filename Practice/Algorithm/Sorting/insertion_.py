# # Insertion Sort
# # -

def insertion_sort(lt):
    # 두번째 인덱스 부터 시작
    for i in range(1, len(lt)):
        # j는 처음인덱스 부터 i까지
        for j in range(i, 0, -1):
            if lt[j] < lt[j-1]:
                lt[j], lt[j-1] = lt[j-1], lt[j]
            else:
                break

def test(n):
    import random as r
    cnt = 0
    while cnt < n:
        lt = r.sample(range(100), 30)
        print('original :', lt)
        insertion_sort(lt)
        for i in range(len(lt)-1):
            if lt[i] > lt[i+1]:
                return print('sorting failed :', lt)
        print('sorted :', lt)
        cnt+=1
    return print('sorting success')

test(10000)