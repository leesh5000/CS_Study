# isalpha() : 문자열이 문자이면 True, 아니면 False
# isdigit() : 숫자처럼 생겼으면 True, 3²도 True
# isnumeric() : 숫자를 표현하는 텍스트는 True, ½도 숫자를 표현하니까 True
# isdecimal() : int()로 즉시 변환이 가능한 문자들, 즉 0-9까지의 문자이면 True
# -> 안전하게 변환하려면 isdecimal() 쓰기

lt = "t0a1"
for x in lt:
    if x.isdecimal():
        print(x)