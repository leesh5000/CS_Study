import sys
from queue import deque
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n, k = map(int, input().split())
    dq = deque([i for i in range(n)])
    while len(dq)!=1:
        for i in range(k):
            item = dq.popleft()
            if i!=k-1:
                dq.append(item)
    print(dq.pop()+1)