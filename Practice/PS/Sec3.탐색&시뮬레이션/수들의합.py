# 이 문제의 경우 시간복잡도 O(n^2), O(n)의 풀이가 있음

import sys
for f in range(1,6):
    sys.stdin = open('./PS/source/in{}.txt'.format(f))

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 경우의수
    ans = 0
    lt = 0
    rt = 1
    # tot는 lt~rt-1까지의 합
    tot = a[0]

    """ solution1 - O(n) """
    while True:
        if tot < m:
            if rt < n:
                tot += a[rt]
                rt += 1
            else:
                break
        elif tot == m:
            tot -= a[lt]
            lt += 1
            ans += 1
        else:
            tot -= a[lt]
            lt += 1
    print(ans)

    """ solution2 - O(n^2) """
    # for i in range(len(a)):
    #     # 현재 값
    #     cur = a[i]
    #     # 다음까지 연속할지 결정
    #     seq = True
    #     # 만약, 현재값이 m과 같으면, 연속된 값을 찾을필요 없으므로 continue한다.
    #     if cur == m:
    #         continue
    #     for j in range(i+1, len(a)):
    #         # 만약, seq가 True이면 연속된 수이므로 다음 값을 더해준다.
    #         if seq == True:
    #             cur += a[j]
    #             # 다음 값을 더해주었는데, 현재까지의 값이 m을 넘어버렸다면, seq를 False로 만든다.
    #             if cur > m:
    #                 seq = False
    #             # 현재까지의 값이 아직 m보다 작다면, 연속된 값을 더 더해주기위해 seq를 True로 만든다.
    #             elif cur < m:
    #                 seq = True
    #             # 현재까지의 값이 m과 같다면, cnt를 1 늘려주고 for문을 빠져나온다.
    #             else:
    #                 ans += 1
    #                 break
    #         else:
    #             break
    # print(ans)