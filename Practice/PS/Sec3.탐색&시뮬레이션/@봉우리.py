import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i), 'r')
    # sys.stdin = open("./PS/source/input.txt", 'r')
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        a[i].insert(0, 0)
        a[i].append(0)
    a.insert(0, [0 for _ in range(n+2)])
    a.append([0 for _ in range(n+2)])
    # 봉우리 정보
    b = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 봉우리를 찾았으면,
            if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and \
                a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]:
                    # 봉우리를 찾았는데, 해당위치의 상하좌우 중에 봉우리가 있었다면,
                    if b[i-1][j] == 1 or b[i+1][j] == 1 or \
                        b[i][j-1] == 1 or b[i][j+1]:
                        # 해당 봉우리 위치에 다시 0을 넣어준다.
                        if b[i-1][j] == 1:
                            b[i-1][j] = 0
                        elif b[i+1][j] == 1:
                            b[i+1][j] = 0
                        elif b[i][j-1] == 1:
                            b[i][j-1] = 0
                        else:
                            b[i][j+1] = 0
                    # 현재 위치에 봉우리 표시
                    b[i][j] = 1
            # 봉우리를 못 찾았으면, 다음위치 확인하기
            else:
                continue
    # 여기까지 왔으면, 봉우리들을 모두 더해준다.
    cnt = 0
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j] == 1:
                cnt += 1
    print(cnt)


                
            
