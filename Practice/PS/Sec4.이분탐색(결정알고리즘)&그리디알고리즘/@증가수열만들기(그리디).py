import sys
from collections import deque
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n = int(input())
    a = list(map(int, input().split()))
    left = 0
    right = len(a)-1
    b = []
    while left <= right:
        if len(b)==0:
            if a[left] > a[right]:
                b.append([a[right], 'R'])
                right -= 1
            else:
                b.append([a[left], 'L'])
                left += 1
        else:
            small = []
            large = []
            if a[left] > a[right]:
                small = [a[right], 'R']
                large = [a[left], 'L']
            else:
                small = [a[left], 'L']
                large = [a[right], 'R']
            if large[0] < b[-1][0]:
                break
            else:
                if b[-1][0] > small[0] and b[-1][0] < large[0]:
                    b.append(large)
                    if large[1] == 'L':
                        left += 1
                    else:
                        right -= 1
                else:
                    b.append(small)
                    if small[1] == 'L':
                        left += 1
                    else:
                        right -= 1
    print(len(b))
    for x in b:
        print(x[1], end='')
    print()
                
