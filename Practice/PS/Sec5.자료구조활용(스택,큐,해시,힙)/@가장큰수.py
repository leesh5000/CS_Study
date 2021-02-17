import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    num, m = map(int, input().split())
    num = list(map(int, str(num)))
    stack = []
    for n in num:
        while stack and stack[-1] < n and m != 0:
            stack.pop()
            m -= 1
        stack.append(n)
    if m != 0:
        stack = stack[:-m]
    print("".join(map(str, stack)))
