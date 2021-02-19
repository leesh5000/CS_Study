import sys
for f in range(1, 2):
    sys.stdin = open("./PS/source/in{}.txt".format(f))
    sys.setrecursionlimit(10**6)

    if __name__ == "__main__":
        n, m = map(int, input().split())

        dis = [[float('inf')] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dis[i][i] = 0
        for i in range(m):
            u, v, w = map(int, input().split())
            dis[u][v] = w

        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

        for i in range(1, n+1):
            for j in range(1, n+1):
                if dis[i][j] == float('inf'):
                    print('M', end=' ')
                else:
                    print(dis[i][j], end=' ')
            print()
