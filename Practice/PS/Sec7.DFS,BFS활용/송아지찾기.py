import sys
from collections import deque
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def BFS(S):
        dq = deque()
        dq.append(S)
        dis[S] = 0
        ch[S] = 1
        while dq:
            now = dq.popleft()
            if now == e:
                break
            for next in (now+1, now-1, now+5):
                if 0 < next <= MAX:
                    if ch[next] == 0:
                        dq.append(next)
                        dis[next] = dis[now] + 1
                        ch[next] = 1
    if __name__ == "__main__":
        s, e = map(int, input().split())
        MAX = 10000
        dis = [0] * 10001
        ch = [0] * 10001
        BFS(s)
        print(dis[e])
