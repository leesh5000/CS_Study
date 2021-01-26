import sys
from heapq import heappush, heappop
for i in range(1,2):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    hq = []
    while True:
        n = int(input())
        if n==-1:
            exit(0)
        elif n==0:
            if len(hq)==0:
                print(-1)
                continue
            print(heappop(hq)[1])
        else:
            heappush(hq, (-n, n))
