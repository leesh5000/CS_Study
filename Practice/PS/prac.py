import sys
from collections import deque

for f in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(f))

    if __name__ == "__main__":
        n = int(input())
        coins = list(map(int, input().split()))
        m = int(input())

        dy = [i for i in range(m+1)]
        for coin in coins:
            for i in range(coin, len(dy)):
                dy[i] = min(dy[i], dy[i-coin]+1)

        print(dy[m])
