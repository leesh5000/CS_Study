import sys
for i in range(1,2):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    k, n = map(int, input().split())
    a = []
    for i in range(k):
        a.append(int(input()))

print(a)