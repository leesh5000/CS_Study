"""
결정알고리즘은 항상 답의 범위를 잡는 것이 중요하다.
"""

import sys

def check(a, mid):
    # 놓은 말의 수, 첫번째에는 무조건 놓기
    cnt = 1
    # 마지막 말의 위치
    last_idx = 0
    for i in range(len(a)):
        distance = abs(a[last_idx] - a[i])
        if distance < mid:
            continue
        else:
            cnt += 1
            last_idx = i
    return cnt

def solution(n, c, a):
    a.sort()
    left = a[0]
    right = a[-1]
    res = 0
    while left <= right:
        # 주어진 마구간 중 두 말을 놓을 수 있는 거리
        mid = (left+right)//2
        # 만약, 현재 mid가 c마리를 놓을 수 있다면, 최적해를 찾도록 mid값 조정
        if check(a, mid)>=c:
            if res < mid:
               res = mid
            left = mid+1
        else:
            right = mid-1
    return res

if __name__ == "__main__":
    for i in range(1,6):
        sys.stdin = open("./PS/source/in{}.txt".format(i))
        n, c = map(int, input().split())
        a = []
        for i in range(n):
            a.append(int(input()))
        print(solution(n, c, a))