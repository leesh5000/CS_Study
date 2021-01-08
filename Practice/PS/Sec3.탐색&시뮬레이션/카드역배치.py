import sys
for f in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(f))

    lt = [i for i in range(21)]
    for i in range(10):
        a, b = map(int, input().split())
        for j in range(((b-a)+1)//2):
            lt[a+j], lt[b-j] = lt[b-j], lt[a+j]
    lt.pop(0)
    for x in lt:
        print(x, end=' ')
    print()