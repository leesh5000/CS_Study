# 1. sort 이용하면 nlog(n)
# 2. 다른 알고리즘을 이용하면 n번만에 가능
# - 강의로 최적화 된 코드보기

import sys
for f in range(1,6):
    sys.stdin = open('./PS/source/in{}.txt'.format(f))
    
    n1 = int(input())
    l1 = list(map(int, input().split()))
    n2 = int(input())
    l2 = list(map(int, input().split()))
    
    """ solution1 """
    # n3 = n1 + n2
    # l3 = []
    # for x in l1:
    #     l3.append(x)
    # for x in l2:
    #     l3.append(x)
    # l3.sort()

    """ solution2 """
    p1 = 0
    p2 = 0
    l3 = []
    for _ in range(n1+n2):
        if p1 != len(l1) and p2 != len(l2):
            if l1[p1] <= l2[p2]:
                l3.append(l1[p1])
                p1 += 1
            else:
                l3.append(l2[p2])
                p2 += 1
        else:
            if p1 == len(l1):
                while p2 != len(l2):
                    l3.append(l2[p2])
                    p2 += 1
            else:
                while p1 != len(l1):
                    l3.append(l1[p1])
                    p1 += 1

    for x in l3:
        print(x, end=' ')
    print()