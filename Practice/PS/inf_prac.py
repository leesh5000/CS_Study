import sys
from heapq import heappush, heappop
from collections import deque

global T
T = 1
while T < 6:
    sys.stdin = open("./source/in%d.txt" % T)

    board = [list(map(int, input().split())) for _ in range(7)]
    ck = [[0] * 7 for _ in range(7)]
    ck[0][0] = 0
    dq = deque()
    dq.append((0, 0))
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while dq:
        now = dq.popleft()
        for i in range(4):
            if 0 <= now[0]+dr[i] < 7 and 0 <= now[1]+dc[i] < 7 and board[now[0]+dr[i]][now[1]+dc[i]] == 0:
                board[now[0]+dr[i]][now[1]+dc[i]] = 1
                ck[now[0]+dr[i]][now[1]+dc[i]] = ck[now[0]][now[1]] + 1
                dq.append((now[0]+dr[i], now[1]+dc[i]))

    print(ck[6][6])
    T += 1
