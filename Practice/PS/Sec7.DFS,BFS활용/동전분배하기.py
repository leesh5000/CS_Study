import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(L, A, B, C):
        global smallest
        if L == n:
            if A == B or A == C or B == C:
                return
            if A == 0 or B == 0 or C == 0:
                return
            if smallest > max(A, B, C)-min(A, B, C):
                smallest = max(A, B, C)-min(A, B, C)
        else:
            DFS(L+1, A+coins[L], B, C)
            DFS(L+1, A, B+coins[L], C)
            DFS(L+1, A, B, C+coins[L])

    if __name__ == "__main__":
        n = int(input())
        coins = []
        for _ in range(n):
            coins.append(int(input()))
        smallest = 2147000000
        DFS(0, 0, 0, 0)
        print(smallest)
