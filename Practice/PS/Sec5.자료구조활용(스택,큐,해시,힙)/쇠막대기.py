import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    bar = str(input())
    stack = []
    cnt = 0
    for x in bar:
        if x == '(':
            stack.append(x)
        else:
            if stack[-1] == '(':
                stack.pop()
                cnt += len(stack)
    print(cnt+1)
