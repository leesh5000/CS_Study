# import sys
# for i in range(1,6):
#     sys.stdin = open('./PS/source/in{}.txt'.format(i), 'r')

#     n = int(input())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     m = int(input())
#     for i in range(m):
#         r, d, c = map(int, input().split())
#         if d==0:
#             for _ in range(c):
#                 a[r-1].append(a[r-1].pop(0))
#         else:
#             for _ in range(c):
#                 a[r-1].insert(0, a[r-1].pop())
#     res = 0
#     s = 0
#     e = n-1
#     for i in range(n):
#         for j in range(s, e+1):
#             res += a[i][j]
#         if i < n//2:
#             s += 1
#             e -= 1
#         else:
#             s -= 1
#             e += 1
#     print(res)

import sys
for i in range(1,6):
    sys.stdin = open('./PS/source/in{}.txt'.format(i), 'r')

    n = int(input())
    for _ in range(n):
        