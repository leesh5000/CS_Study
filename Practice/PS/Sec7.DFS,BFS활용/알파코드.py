import sys
for i in range(1, 2):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(L, word):
        if L == length:
            pass
        else:
            for i in range(1, 27):
                if i < 10:
                    DFS(L+1, word+chr(ord("A")-1+i))
                if i >= 10 and

    if __name__ == "__main__":
        num = str(input())
        length = len(num)
        DFS(0, '')
