# 자릿수의 합

for i in range(1,6):
    f1 = open('./PS/source/in{}.txt'.format(i), 'r')
    
    n = int(f1.readline())
    lt = list(map(int, f1.readline().split()))

    ans = 1
    max_value = -2147000000

    # 리스트의 돌면서    
    for i in lt:
        tmp = 0
        # 리스트 값을 문자열로 변환하고 그 문자열을 하나씩 tmp에 더하기
        for j in str(i):
            tmp += int(j)
        # 만약, i의 모든 자릿수를 더한 값이 max_value보다 크다면,
        if tmp > max_value:
            max_value = tmp
            ans = i
        
    print(ans)