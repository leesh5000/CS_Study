import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n = int(input())
    def dfs(n):
        if n==0:
            return
        else:
            dfs(n//2)
            print(n%2, end='')
    dfs(n)
    print()