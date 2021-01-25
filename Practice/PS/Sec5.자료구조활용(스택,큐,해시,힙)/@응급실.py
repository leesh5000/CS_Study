"""
파이썬 any함수 사용
"""
import sys
from collections import deque
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n, m = map(int, input().split())
    a = [[pos, value] for pos, value in enumerate(list(map(int, input().split())))]
    a = deque(a)
    cnt = 0
    target = a[m]
    while True:
        current = a.popleft()
        cure = False
        for i in range(len(a)):
            if current[1] < a[i][1]:
                a.append(current)
                break
            else:
                if i==len(a)-1:
                    cure = True
                    cnt += 1
                continue
        if cure and current==target:
            break
    print(cnt)
    