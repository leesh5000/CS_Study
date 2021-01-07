# 문자열 입력 받을때는 항상 \n 이 있는지 확인할 것
# \n 은 strip() 함수로 없앨수있음
# split()은 나눠주는 함수

for f in range(1,6):
    f1 = open('./PS/source/in{}.txt'.format(f), 'r')
    n = int(f1.readline())
    for i in range(1,n+1):
        s = f1.readline().strip().lower()
        if s == s[::-1]:
            print("#%d YES" %(i))
        else:
            print("#%d NO" %(i))
    print()