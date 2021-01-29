import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    def DFS(v):
        global cnt
        if v == m:
            for i in range(m):
                print(res[i], end=' ')
            print()
            cnt += 1
        else:
            for i in range(1, n+1):
                if use[i]:
                    continue
                use[i] = True
                res[v] = i
                DFS(v+1)
                use[i] = False
    if __name__ == "__main__":
        n, m = map(int, input().split())
        use = [False for _ in range(n+1)]
        res = [0] * m
        cnt = 0
        DFS(0)
        print(cnt)