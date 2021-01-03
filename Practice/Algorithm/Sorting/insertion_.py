# # Insertion Sort
# # -

# def insertion_sort(lt: []) -> []:
#     # 리스트의 길이가 1이면 그냥 리턴
#     if len(lt) == 1:
#         return
#     # 두번째 데이터부터, 마지막 데이터까지
#     for i in range(1, len(lt)):
#         # i번째부터, 0번째까지 -1을 해가면서
#         for j in range(i, 0, -1):
#             # 현재 인덱스와 그 전 인덱스의 값을 비교한다.
#             if lt[j-1] > lt[j]:
#                 lt[j-1], lt[j] = lt[j], lt[j-1]
#             # 만약, 그 전 데이터가 더 작다면, 더 이상 for문을 돌 필요가 없다.
#             else:
#                 break

def insertion_sort(lt: []) -> []:
    for i in range(1, len(lt)):
        for j in range(i, 0, -1):
            if lt[j-1] > lt[j]:
                lt[j-1], lt[j] = lt[j], lt[j-1]
            else:
                break

def test(n):
    import random as r
    cnt = 0
    while cnt < n:
        lt = r.sample(range(1000), 20)
        print('original :', lt)
        insertion_sort(lt)
        for i in range(len(lt)-1):
            if lt[i] > lt[i+1]:
                return print('sorting failed :', lt)
        print('sorted :', lt)
        cnt+=1
    return print('sorting success')

test(10)