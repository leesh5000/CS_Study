import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(L, sum):
        global cnt
        if sum > T or L > k:
            return
        if L == k:
            if sum == T:
                cnt += 1
        else:
            for i in range(coins[L][1]+1):
                DFS(L+1, sum+coins[L][0]*i)

    if __name__ == "__main__":
        T = int(input())
        k = int(input())
        coins = []
        for _ in range(k):
            coin, count = map(int, input().split())
            coins.append((coin, count))
        cnt = 0
        DFS(0, 0)
        print(cnt)
