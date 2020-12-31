# Bubble Sort
# - O(n^2)의 시간복잡도

# def bubble_sort(lt: list)->list:
#     # 최악의 경우, 배열의 길이 - 1 만큼 돌아야함
#     for i in range(len(lt)-1):
#         # 중간에 다 정렬이 완료된 경우를 판별하기 위한 플래그
#         swap = False
#         # 두 수를 뽑아낼 반복문, 한번 버블정렬 싸이클을 돌때마다 뒤에 숫자들이 정렬된다.
#         for j in range(len(lt)-i-1):
#             if lt[j] > lt[j+1]:
#                 lt[j], lt[j+1] = lt[j+1], lt[j]
#                 # 한번이라도 스왑이 발생하면, True로 한다.
#                 swap = True                
#         # 한번도 swap이 발생하였다면, 더 이상 반복문을 돌 필요가 없으므로 break
#         if swap == False:
#             break

# def bubble_sort(lt: []) -> []:
#     for i in range(len(lt)-1):
#         swap = False
#         for j in range(len(lt)-i-1):
#             if lt[j] > lt[j+1]:
#                 lt[j], lt[j+1] = lt[j+1], lt[j]
#                 swap = True
#         if swap == False:
#             break

import random as r

lt = r.sample(range(10000), 20)
print('not sorted :',lt)
bubble_sort(lt)
print('sorted :',lt)