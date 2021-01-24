# isalpha() : 문자열이 문자이면 True, 아니면 False
# isdigit() : 숫자처럼 생겼으면 True, 3²도 True
# isnumeric() : 숫자를 표현하는 텍스트는 True, ½도 숫자를 표현하니까 True
# isdecimal() : int()로 즉시 변환이 가능한 문자들, 즉 0-9까지의 문자이면 True
# -> 안전하게 변환하려면 isdecimal() 쓰기

import sys
for i in range(3,4):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    a = str(input())
    stack = []
    print(a)
    for x in a:
        if x.isdecimal():
            print(x, end='')
        else:
            if len(stack)==0:
                stack.append(x)
                continue
            elif x=='+' or x=='-':
                while stack:
                    if stack[-1] != '(':
                        print(stack.pop(), end='')
                        break
                    print(stack.pop(), end='')
            elif x=='*' or x=='/':
                if stack[-1] != '(' and stack[-1] != '+' and stack[-1] != '-':
                    print(stack.pop(), end='')
            elif x==')':
                while True:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    print(stack.pop(), end='')
                continue
            else:
                stack.append(x)
                continue
            stack.append(x)
    while stack:
        print(stack.pop(), end='')
    print()