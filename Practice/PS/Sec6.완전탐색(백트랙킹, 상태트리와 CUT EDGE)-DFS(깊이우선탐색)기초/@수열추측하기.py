import sys
for i in range(5,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    def DFS(v, sum):
        if v==n and sum==f:
            for x in permu:
                print(x, end=' ')
            sys.exit(0)
        else:
            for i in range(1, n+1):
                if used[i]:
                    continue
                used[i] = True
                permu[v] = i
                DFS(v+1, sum+(permu[v]*bi[v]))
                used[i] = False
    if __name__ == "__main__":
        n, f = map(int, input().split())
        used = [False] * (n+1)
        permu = [0] * n
        res = []
        bi = [1] * n
        for i in range(1, n):
            bi[i] = (bi[i-1] * (n-i)) // i
        DFS(0,0)