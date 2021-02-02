import sys
for i in range(1, 6):
    sys.stdin = open('./PS/source/in{}.txt'.format(i), 'r')
    s = str(input())
    res = 0
    for c in s:
        if c.isdecimal():
            res = res * 10 + int(c)
    cnt = 0
    for i in range(1, res+1):
        if res % i == 0:
            cnt += 1
    print(res, cnt, sep='\n')
    print()
