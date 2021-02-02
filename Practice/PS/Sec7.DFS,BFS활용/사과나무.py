import sys
from collections import deque
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    check = [[0 for _ in range(n)] for _ in range(n)]
    Q = deque()
    Q.append([n//2, n//2])
    check[n//2][n//2] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    L = 0
    sum = 0
    sum += board[n//2][n//2]
    while Q:
        if L == n//2:
            break
        size = len(Q)
        for i in range(size):
            base = Q.popleft()
            for i in range(4):
                next = [base[0] + dx[i], base[1] + dy[i]]
                if check[next[0]][next[1]]:
                    continue
                check[next[0]][next[1]] = 1
                sum += board[next[0]][next[1]]
                Q.append(next)
        L += 1
    print(sum)
