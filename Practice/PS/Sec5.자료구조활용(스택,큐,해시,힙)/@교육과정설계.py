import sys
from collections import deque
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    s = str(input())
    n = int(input())
    a = []
    for _ in range(n):
        a.append(str(input()))
    for i in range(n):
        dq = deque(a[i])
        expected = 0
        correct = True
        now = ''
        while dq:
            if correct == False:
                break
            item = dq.popleft()
            if item in s:
                if item in now:
                    break
                elif item == s[expected]:
                    correct = True
                    now += s[expected]
                    expected += 1
                    if expected == len(s):
                        break
                else:
                    correct = False
        if correct and now==s:
            print("#%d YES"%(i+1))
        else:
            print("#%d NO"%(i+1))
    print()

