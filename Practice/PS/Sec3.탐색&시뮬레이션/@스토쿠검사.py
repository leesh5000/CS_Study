import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i), 'r')
    a = [list(map(int, input().split())) for _ in range(9)]
    def solution(a):
        # 가로 & 세로 검사
        for i in range(9):
            r_check = [0] * 10
            c_check = [0] * 10
            for j in range(9):
                if r_check[a[i][j]] == 0:
                    r_check[a[i][j]] = 1
                else:
                    return False
                if c_check[a[j][i]] == 0:
                    c_check[a[j][i]] = 1
                else:
                    return False
        # 3x3 보드검사
        for i in range(3):
            for j in range(3):
                b_check = [0]*10
                for k in range(3):
                    for l in range(3):
                        if b_check[a[i*3+k][j*3+l]] == 0:
                            b_check[a[i*3+k][j*3+l]] = 1
                        else:
                            return False
        return True
    
    if solution(a):
        print("YES")
    else:
        print("NO")