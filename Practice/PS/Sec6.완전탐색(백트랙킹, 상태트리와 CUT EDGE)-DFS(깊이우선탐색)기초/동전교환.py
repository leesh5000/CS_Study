'''
DFS는 의외로 불필요한 것들까지 다 탐색하기 때문에 Cut-Of-The-Edge를 하면 생각보다 크게 성능향샹이 된다.
DFS + Greedy
'''
import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    def DFS(select):
        global length
        if sum(select) == m:
            if len(select) < length:
                length = len(select)
        else:
            for i in range(len(coins)):
                select.append(coins[i])
                if sum(select) > m or len(select) > length:
                    select.pop()
                    continue
                DFS(select)
                select.pop()
    if __name__ == "__main__":
        n = int(input())
        coins = list(map(int, input().split()))
        coins.sort(reverse=True)
        m = int(input())
        length = 2147000000
        DFS([])
        print(length)