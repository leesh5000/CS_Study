import sys
for i in range(1, 6):
    sys.setrecursionlimit(10**6)
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(L, S):
        global res, ans
        if L == m:
            dist = [0] * len(house)
            for i in range(len(house)):
                minimum = 2147000000
                for j in range(len(res)):
                    temp = abs(house[i][0]-res[j][0]) + \
                        abs(house[i][1]-res[j][1])
                    if minimum > temp:
                        minimum = temp
                dist[i] = minimum
            if ans > sum(dist):
                ans = sum(dist)
        else:
            for i in range(S, len(pizza)):
                res[L] = pizza[i]
                DFS(L+1, i+1)

    if __name__ == "__main__":
        n, m = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]

        house = []
        pizza = []
        res = [0] * m
        ans = 2147000000

        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    house.append((i, j))
                elif board[i][j] == 2:
                    pizza.append((i, j))

        DFS(0, 0)
        print(ans)
