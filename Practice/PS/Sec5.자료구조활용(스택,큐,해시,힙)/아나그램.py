'''
get()함수 사용
'''
import sys
from collections import deque
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    m = input()
    a = dict()
    for x in m:
        if x in a:
            a[x] += 1
        else:
            a[x] = 1
    for y in input():
        if y in a:
            a[y] -= 1
        else:
            print("NO")
    check = a.values()
    if any(x!=0 for x in check):
        print("NO")
    else:
        print("YES")
    
    