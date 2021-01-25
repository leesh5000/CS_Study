import sys
from collections import deque
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n = int(input())
    a = dict()
    for _ in range(n):
        a[str(input())] = 1
    for _ in range(n-1):
        word = str(input())
        a[word] = 0
    for key, value in a.items():
        if value==1:
            print(key)