"""
[이분검색&결정알고리즘]
- 어느 범위 안에 답이 있다고 확실시 될 때, 이분검색으로 결정
"""

import sys
for f in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(f))
    k, n = map(int, input().split())
    a = []
    for _ in range(k):
        a.append(int(input()))
    lt = 0
    rt = max(a)
    res = -2147000000
    while lt <= rt:
        mid = (lt+rt)//2
        cnt = 0
        for x in a:
            cnt += x // mid
        if cnt >= n:
            if mid > res:
                res = mid
            lt = mid+1
        else:
            rt = mid-1
    print(res)
