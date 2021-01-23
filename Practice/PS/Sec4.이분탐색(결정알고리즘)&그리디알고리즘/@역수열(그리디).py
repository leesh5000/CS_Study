import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    ans = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        cnt = 0
        base = 0
        for x in ans[1:]:
            if x != 0:
                base += 1
                continue
            if cnt == a[i]:
                ans[cnt+base+1] = i
                break
            if x == 0:
                cnt += 1
    print(ans[1:])