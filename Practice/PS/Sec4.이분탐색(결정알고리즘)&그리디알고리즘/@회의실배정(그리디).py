"""
그리디 알고리즘
- 그리디는 거의 대부분이 정렬이다.
"""
import sys

def solution(n, a):
    cur_end = 0
    cnt = 0
    for next_start, next_end in a:
        if cur_end <= next_start:
            cnt += 1
            cur_end = next_end
    return cnt

if __name__ == "__main__":
    for i in range(1,6):
        sys.stdin = open("./PS/source/in{}.txt".format(i))
        n = int(input())
        a = []
        for i in range(n):
            a.append(list(map(int, input().split())))
        a.sort(key= lambda x : (x[1], x[0]))
        print(solution(n, a))