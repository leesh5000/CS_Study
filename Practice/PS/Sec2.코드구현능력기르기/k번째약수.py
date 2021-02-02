import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n, k = map(int, input().split())
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    divisor.sort()
    if len(divisor) < k:
        print(-1)
    else:
        print(divisor[k-1])
