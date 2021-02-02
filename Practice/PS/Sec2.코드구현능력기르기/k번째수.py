import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    T = int(input())
    for _ in range(T):
        N, s, e, k = map(int, input().split())
        a = list(map(int, input().split()))
        a = a[s-1:e]
        a.sort()
        print(a[k-1])
    print()
