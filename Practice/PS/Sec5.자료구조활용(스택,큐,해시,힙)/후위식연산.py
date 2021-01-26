import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    s = str(input())
    stack = []
    for x in s:
        if x.isdecimal():
            stack.append(x)
        else:
            if x=='+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
            elif x=='-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
            elif x=='*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a*b)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a/b)
    print(stack.pop())
