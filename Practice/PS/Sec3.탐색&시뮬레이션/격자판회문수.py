import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    # check function
    def isPalindrome(n):
        for i in range(len(n)//2):
            if n[i] != n[len(n)-1-i]:
                return False
        return True
    # rcheck
    for i in range(3):
        for j in range(7):
            # row check
            if isPalindrome(board[j][i:i+5]):
                cnt += 1
    # col check
    for i in range(7):
        for j in range(3):
            temp = []
            for k in range(5):
                temp.append(board[j+k][i])
            if isPalindrome(temp):
                cnt += 1
    print(cnt)