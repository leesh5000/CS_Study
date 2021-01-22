'''
이 문제는 이중for문을 피하는 것이 중요
'''
import sys

for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    n = int(input())
    candidate = []
    for i in range(n):
        candidate.append(list(map(int, input().split())))
    candidate.sort(reverse=True)
    largest = 0
    cnt = 0
    for x in candidate:
        if largest < x[1]:
            largest = x[1]
            cnt += 1
    print(cnt)