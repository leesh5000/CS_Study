'''
get()함수 사용
'''
import filecmp
import sys
for i in range(1,6):
    sys.stdout = open("./PS/source/myout{}.txt".format(i), 'w')
    
    sys.stdin = open("./PS/source/in{}.txt".format(i), 'r')
    m = input()
    a = dict()
    for x in m:
        if x in a:
            a[x] += 1
        else:
            a[x] = 1
    for y in input():
        if y in a:
            a[y] -= 1
        else:
            print("NO", end='')
    check = a.values()
    if any(x!=0 for x in check):
        print("NO", end='')
    else:
        print("YES", end='')
    
    sys.stdout = sys.__stdout__
    if filecmp.cmp("./PS/source/in{}.txt".format(i), "./PS/source/myout{}.txt".format(i)):
        print("Test #%d : Success"%(i))
    else:
        print("Test #%d : Fail"%(i))