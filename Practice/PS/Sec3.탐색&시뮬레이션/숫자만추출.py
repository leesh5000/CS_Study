import sys
for i in range(1,6):
    sys.stdin = open('./PS/source/in{}.txt'.format(i), 'r')
    
    s = input()
    # 추출한 숫자
    res = 0
    # 숫자 추출하기
    for c in s:
        if c.isdecimal():
            res = res * 10 + int(c)
    print(res)
    # 약수의 개수
    cnt = 0
    # 약수의 개수 구하기
    for i in range(1, res+1):
        if res%i==0:
            cnt += 1
    print(cnt)
            
            