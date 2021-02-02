'''
최단거리문제는 BFS
-> 한 번만에 갈 수 있는거 전부 방문, 두번만에 전부 방문, 세번만에 ... 
DFS는 최단거리를 보장하지 않는다.
'''

import sys
from collections import deque
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    board = [list(map(int, input().split())) for _ in range(7)]
    start = (0, 0)
    Q = deque()
    Q.append(start)
    dis = [[0 for _ in range(7)] for _ in range(7)]
    dis[start[0]][start[1]] = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    move = 0
    while Q:
        now = Q.popleft()
        if now[0] == 6 and now[1] == 6:
            break
        for i in range(4):
            next = [now[0]+dr[i], now[1]+dc[i]]
            if next[0] < 0 or next[0] > 6 or next[1] < 0 or next[1] > 6:
                continue
            if board[next[0]][next[1]] == 1:
                continue
            if dis[next[0]][next[1]]:
                continue
            if next[0] == 0 and next[1] == 0:
                continue
            dis[next[0]][next[1]] = dis[now[0]][now[1]] + 1
            Q.append(next)
    print(dis[6][6])
