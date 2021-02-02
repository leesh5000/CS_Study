import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(L, sum):
        global res
        if L == k:
            if sum > 0:
                res.add(sum)
        else:
            DFS(L+1, sum+a[L])
            DFS(L+1, sum-a[L])
            DFS(L+1, sum)

    if __name__ == "__main__":
        k = int(input())
        a = list(map(int, input().split()))
        res = set()
        DFS(0, 0)
        print(sum(a)-len(res))
