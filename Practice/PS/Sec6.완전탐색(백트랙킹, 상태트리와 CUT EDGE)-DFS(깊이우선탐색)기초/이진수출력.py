import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def Binary(n):
        if n < 1:
            return
        else:
            Binary(n//2)
            print(n % 2, end='')

    if __name__ == "__main__":
        n = int(input())
        Binary(n)
        print()
