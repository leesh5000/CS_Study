import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    sys.setrecursionlimit(10**6)

    n = int(input())
    arr = list(map(int, input().split()))
    dy = [0] * n
    dy[0] = 1
    res = 0

    for i in range(1, n):
        max = 0
        for j in range(i-1, -1, -1):
            if arr[i] > arr[j] and dy[j] > max:
                max = dy[j]
        dy[i] = max + 1
        if dy[i] > res:
            res = dy[i]

    print(res)
