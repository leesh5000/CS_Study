import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    bar = str(input())
    stack = []
    cnt = 0
    offset = 0
    for b in bar:
        if b=='(':
            offset += 1
        else:
            if len(stack)==0:
                break
            if stack[-1] == '(':
                offset -= 1
                cnt += offset
            else:
                offset -= 1
                cnt += 1
        stack.append(b)
    print(cnt)