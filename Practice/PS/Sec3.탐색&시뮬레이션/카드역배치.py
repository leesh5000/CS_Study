import sys
for f in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(f))
    card = [i for i in range(21)]
    for _ in range(10):
        a, b = map(int, input().split())
        for i in range((b-a)//2+1):
            card[a+i], card[b-i] = card[b-i], card[a+i]
    print(card[1:])
