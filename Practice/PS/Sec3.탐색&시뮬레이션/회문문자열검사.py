# 문자열 입력 받을때는 항상 \n 이 있는지 확인할 것
# \n 은 strip() 함수로 없앨수있음
# split()은 나눠주는 함수

import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    n = int(input())
    for i in range(n):
        s = input().strip().lower()
        for j in range(len(s)//2):
            if s[j] != s[len(s)-1-j]:
                print("#%d NO" % (i+1))
                break
        else:
            print("#%d YES" % (i+1))

    print()
