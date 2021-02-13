import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    n = int(input())
    a = list(map(int, input().split()))

    mean = round(sum(a)/n)
    min = [2147000000, 0, 0]

    for i in range(len(a)):
        dist = [abs(a[i]-mean), a[i]]
        if dist[0] < min[0]:
            min[0] = dist[0]
            min[1] = dist[1]
            min[2] = i+1
        elif dist[0] == min[0]:
            if dist[1] > min[1]:
                min[1] = dist[1]
                min[2] = i+1
        else:
            continue

    print(mean, min[2])
