for i in range(1,6):
    f1 = open('./PS/source/in{}.txt'.format(i), 'r')

    n = int(f1.readline())
    lt = list(map(int, f1.readline().split()))

    sum = 0
    acm = 0

    for x in lt:
        if x == 1:
            acm += 1
            sum += acm
        else:
            acm = 0

    f2 = open('./PS/source/my_out{}.txt'.format(i), 'w')
    f2.write("%d" %(sum))