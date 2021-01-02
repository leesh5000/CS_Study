from filecmp import cmp

# in{}의 개수만큼 for문
for i in range(1,6):
    with open('./PS/in{}.txt'.format(i), 'r') as f1:
        with open('./PS/my_out{}.txt'.format(i), 'w') as f2:
            t = int(f1.readline())
            for j in range(t):
                n,s,e,k = map(int, f1.readline().split())
                lt = list(map(int, f1.readline().split()))

                """ solution """
                lt = lt[s-1:e]
                lt.sort()
                print("#%d %d" % (j+1,lt[k-1]))

                """ file write """
                f2.write("#%d %d" % (j+1,lt[k-1]))
                if j+1!=t:
                    f2.write('\n')


            """ file comparison """
            if cmp('./PS/my_out{}.txt'.format(i), './PS/out{}.txt'.format(i)):
                print('Test #%d: right' % (i))
            else:
                print('Test #%d: wrong' % (i))