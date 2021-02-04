import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(L, S):
        global ans
        if L == 3:
            ans.append(sum(res))
        else:
            for i in range(S, n):
                res[L] = a[i]
                DFS(L+1, i+1)

    if __name__ == "__main__":
        f1 = open('./PS/source/in{}.txt'.format(i), 'r')
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        res = [0] * 3
        ans = []
        DFS(0, 0)
        print(list(sorted(set(ans), reverse=True))[k-1])
