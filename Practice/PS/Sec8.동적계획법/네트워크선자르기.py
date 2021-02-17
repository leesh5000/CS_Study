'''
동적프로그래밍
- 복잡한 문제를 잘개 쪼개어 해결한 후, 그 해를 더 큰 문제를 구하기 위해 활용
- Bottom-Up : 바텀업은 아래서 부터 올라가니까 메모이제이션 할 필요가 없음
- Top-Down : 재귀 + 메모이제이션 - 메모이제이션을 해야 동적프로그래밍!
- 엄밀히 말하면, 동적계획법은 바텀업 방식만을 말한다. 즉, 1차원배열이나 2차원 배열을 사용하는 방식
- 원래 탑다운 방식은 그냥 재귀(순환알고리즘) + 메모이제이션을 하기 때문에 넓은 의미에서 동적계획법이라고 한다.
- 하지만, 엄밀히 말하면, 작은 문제에서 큰 문제로 뻗어나가는 바텀업 방식이 진짜 동적계획법이다.

DP vs Greedy의 차이
'''

import sys
for i in range(1, 2):
    # sys.stdin = open("./PS/source/in{}.txt".format(i))
    sys.setrecursionlimit(10**6)

    # def DFS(n):
    #     global dy
    #     if dy[n] > 0:
    #         return dy[n]
    #     if n == 0:
    #         return
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     if n > 2:
    #         dy[n] = DFS(n-1)+DFS(n-2)
    #         return dy[n]

    if __name__ == "__main__":
        n = int(input())
        dy = [0] * (n+1)
        # DFS(n)
        dy[1] = 1
        dy[2] = 2
        for i in range(3, n+1):
            dy[i] = dy[i-1] + dy[i-2]

        print(dy[n])
