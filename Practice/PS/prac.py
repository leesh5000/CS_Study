import sys
from collections import deque

for f in range(1, 2):
    sys.stdin = open("./PS/source/in{}.txt".format(f))

    if __name__ == "__main__":
        n, m = map(int, input().split())
        graph = [[0] * (n+1) for _ in range(n+1)]

        degree = [0] * (n+1)
        Q = deque()

        for _ in range(m):
            u, v = map(int, input().split())
            degree[v] += 1
            print(u, v)
            print(degree)
            print()
            graph[u][v] = 1

        for i in range(1, len(degree)):
            if degree[i] == 0:
                Q.append(i)

        print(Q)

        while Q:
            start = Q.popleft()
            print(start, end=' ')
            for end in range(1, len(graph[start])):
                if graph[start][end] == 1:
                    degree[end] -= 1
                    if degree[end] == 0:
                        Q.append(end)
