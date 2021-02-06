import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    sys.setrecursionlimit(10**6)

    def DFS(n):
        if dy[n] > 0:
            return dy[n]
        if n == 1 or n == 2:
            return n
        else:
            dy[n] = DFS(n-1)+DFS(n-2)
            return dy[n]

    if __name__ == "__main__":
        n = int(input())
        dy = [0] * (n+1)
        DFS(n)
        print(dy[n])
