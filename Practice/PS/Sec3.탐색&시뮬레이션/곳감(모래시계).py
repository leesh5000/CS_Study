import sys
for i in range(1,2):
    sys.stdin = open("./PS/source/in{}.txt".format(i), 'r')
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    m = int(input())
    for i in range(m):
        r, d, c = map(int, input().split())
        if d==0:
            temp = []
            for j in range(n):
                temp[j] = a[r][(j+3)%n]
        else:
            temp = []
            for j in range(n):
                temp[j] = a[r][(j-3)%n]
            a[r] = temp
    res = 0
    s = 0
    e = n-1
    for i in range(n):
        for j in range(s, e+1):
            res += a[i][j]
        if i < n//2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1
    print(res)