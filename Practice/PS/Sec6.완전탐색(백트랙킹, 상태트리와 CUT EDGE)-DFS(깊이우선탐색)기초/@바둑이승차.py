import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))    
    def dfs(cur_idx, sum):
        global largest
        if sum > c:
            return
        if cur_idx == n:
            if sum > largest:
                largest = sum
        else:
            dfs(cur_idx+1, sum+a[cur_idx])
            dfs(cur_idx+1, sum)
    if __name__ == "__main__":
        c,n = map(int, input().split())
        a = []
        for _ in range(n):
            a.append(int(input()))
        largest = -2147000000
        dfs(0,0)
        print(largest)