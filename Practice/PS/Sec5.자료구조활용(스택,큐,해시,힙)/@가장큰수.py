import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n, m = map(int, input().split())
    cnt = m
    n = str(n)
    stack = []
    for x in n:
        while stack and x > stack[-1] and m > 0:
            stack.pop()
            m -= 1
        stack.append(x)
    if m != 0:
        stack = stack[:-m]
    print("".join(map(str, stack)))