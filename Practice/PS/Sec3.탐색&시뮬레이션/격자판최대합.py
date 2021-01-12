import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))    
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    max = -2147000000
    # 가로, 세로의 합
    for i in range(n):
        row_sum = col_sum = 0
        for j in range(n):
            row_sum += a[i][j]
            col_sum += a[j][i]
            if row_sum > max:
                max = row_sum
            if col_sum > max:
                max = col_sum
    # 대각선의 합
    lr_dia_sum = rl_dia_sum = 0 
    for i in range(n):
        lr_dia_sum += a[i][i]
        rl_dia_sum += a[i][n-i-1]
        if lr_dia_sum > max:
            max = lr_dia_sum
        if rl_dia_sum > max:
            max = rl_dia_sum
    print(max)