import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))
    l = int(input())
    heights = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        heights.sort(reverse=True)
        heights[0] -= 1
        heights[-1] += 1
    print(max(heights)-min(heights))