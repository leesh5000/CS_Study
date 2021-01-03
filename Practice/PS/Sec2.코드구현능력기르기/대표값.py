# print(round(12, 1))

for f in range(1,6):
    f1 = open('./PS/source/in{}.txt'.format(f), 'r')
    """ file input """
    n = int(f1.readline())
    lt = list(map(int, f1.readline().split()))

    """ solution """
    min = 2147000000
    score = 2147000000
    # 주의! 파이썬은 round_half_even 방식이므로 4.5와 같이 소수 이하 자리가 정확하게 딱 중간이면 짝수 쪽으로 근사값을 반환한다.
    # 따라서, round쓰면 안되고앞으로 반올림 같은 경우에는 다음과 같이 사용한다.
    avg = sum(lt) / n
    avg = int(avg+0.5)
    for idx, value in enumerate(lt):
        tmp = abs(value - avg)
        if tmp < min:
            min = tmp
            # C++은 변수의 유효범위가 블록({}) 기준, 파이썬은 함수 기준
            score = lt[idx]
            res = idx + 1
        elif tmp == min:
            if score < value:
                score = value
                res = idx + 1
    print(avg, res)

    """ file write """
    f2 = open('./PS/source/my_out{}.txt'.format(f), 'w')
    f2.write('%d %d'%(avg, res))

    """ file comparison """
    from filecmp import cmp
    if cmp('./PS/source/my_out{}.txt'.format(f), './PS/source/out{}.txt'.format(f)):
        print('Test #%d: right' % (f))
    else:
        print('Test #%d: wrong' % (f))

    """ file close """
    f1.close()
    f2.close()