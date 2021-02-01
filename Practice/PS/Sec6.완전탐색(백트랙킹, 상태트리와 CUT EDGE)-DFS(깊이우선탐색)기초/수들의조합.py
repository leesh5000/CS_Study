import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    def DFS(L,s):
        global cnt, multiple
        if L==k:
            if sum(res) % multiple == 0:
                cnt += 1
        else:
            for i in range(s, len(nums)):
                res[L] = nums[i]
                DFS(L+1, i+1)
    if __name__ == "__main__":
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        multiple = int(input())
        res = [0] * k
        cnt = 0
        DFS(0,0)
        print(cnt)