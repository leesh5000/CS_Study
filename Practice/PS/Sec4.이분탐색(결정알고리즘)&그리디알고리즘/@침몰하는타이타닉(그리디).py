'''
파이썬 list와 deque
- list는 pop(0)를 하면, 전체 원소들을 앞으로 당겨온다.
- deque는 popleft()을 해도, 포인터의 위치가 바뀔 뿐 이다.
'''
import sys
from collections import deque
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort()
    check = [False for _ in range(n)]
    cnt = 0
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        boat = m
        cnt += 1
        current = weights[i]
        boat -= current
        for j in range(n-1, -1, -1):
            if check[j]:
                continue
            if boat - weights[j] < 0:
                continue
            else:
                check[j] = True
            break
    print(cnt)