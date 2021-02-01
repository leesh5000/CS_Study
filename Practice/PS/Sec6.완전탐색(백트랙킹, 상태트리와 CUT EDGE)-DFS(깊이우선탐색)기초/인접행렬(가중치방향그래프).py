import sys
for i in range(1,2):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    if __name__ == "__main__":
        n, m = map(int, input().split())
        graph = [[0 for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph[u-1][v-1] = w
        print(graph)