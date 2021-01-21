# 이 문제는 쉬운데, 실수를 할 가능성이 있다.
# 실제 시험장에서 이런 실수를 할 수도 있으니까 주의깊게 보기

for i in range(1, 6):
    f1 = open('./PS/source/in{}.txt'.format(i), 'r')
    n = int(f1.readline())
    lt = []
    for i in range(n):
        lt.append(list(map(int, f1.readline().split())))

    prize = []
    # 리스트에 담긴 사람의 주사위 눈들의 리스트
    for x in lt:
        if x[0]==x[1] and x[1]==x[2]:
            prize.append(10000+x[0]*1000)
            continue
        elif x[0]==x[1] or x[0]==x[2]:
            # 상금구하기
            prize.append(1000+x[0]*100)
        elif x[1]==x[2]:
            # 상금구하기
            prize.append(1000+x[1]*100)
        else:
            # 상금구하기
            prize.append(max(x[0],x[1],x[2])*100)

    print(max(prize))

    f2 = open('./PS/source/my_out{}.txt'.format(i), 'w')
    f2.write("%d" %(max(prize)))