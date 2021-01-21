"""
[이분검색&결정알고리즘]
- 어느 범위 안에 답이 있다고 확실시 될 때, 이분검색으로 결정
"""

import sys
# 현재 길이가 적합한 값인지 체크해주는 함수
def check(a, mid, need):
    cnt = 0
    for i in range(len(a)):
        temp = a[i]
        # # 중간값으로 랜선 만들기
        # while temp - mid >= 0:
        #     temp -= mid
        #     cnt += 1
        cnt += temp//mid
    if cnt < need:
        return False
    else:
        return True

def solution(a, need):
    # 가장 큰 길이를 추출
    max_len = max(a)
    left = 1
    right = max_len
    ans = 0
    # 가장 큰 길이를 기준으로 이분탐색 시작
    while not (left > right):
        mid = (left+right)//2
        # 만약, 현재 mid값이 need를 만족시킨다면, 더 나은 값이 있을수도 있으니 더 큰 길이로 다시 진행
        if check(a, mid, need) and mid > ans:
            ans = mid
            left = mid+1
        else:
            right = mid-1
    return ans

if __name__ == "__main__":
    for i in range(1,6):
        sys.stdin = open("./PS/source/in{}.txt".format(i))
        k, n = map(int, input().split())
        a = []
        for i in range(k):
            a.append(int(input()))
        print(solution(a, n))