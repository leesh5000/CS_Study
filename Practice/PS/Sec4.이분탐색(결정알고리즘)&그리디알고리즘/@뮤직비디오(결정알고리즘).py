import sys

def solution(n, m, a):
    left = 0
    right = sum(a)
    ans = right
    maxx = max(a)
    while left <= right:
        mid = (left+right)//2
        temp = mid
        cnt = 1
        for i in range(len(a)):
            if temp - a[i] >= 0:
                temp -= a[i]
            else:
                cnt += 1
                temp = mid
                temp -= a[i]
        if cnt > m:
            left = mid+1
        else:
            right = mid-1
            if mid < ans and mid >= maxx:
                ans = mid
    return ans

if __name__ == "__main__":
    for i in range(1,6):
        sys.stdin = open("./PS/source/in{}.txt".format(i))
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        print(solution(n, m, a))