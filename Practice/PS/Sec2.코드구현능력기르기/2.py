with open('./PS/input.txt', 'r') as f:
    t = int(f.readline())
    for i in range(t):
        n,s,e,k = map(int, f.readline().split())
        lt = list(map(int, f.readline().split()))

        """ solution """
        lt = lt[s-1:e]
        lt.sort()
        print("#%d %d" % (i+1,lt[k-1]))

