# 파이썬 리스트 컴프리헨션

lt1 = []
for n in range(1,101):
    lt1.append(n)
print(lt1)

lt2 = [x for x in range(1,101)]
print(lt2)

q3 = ["a", "b", "c", "d"]
lt3 = [x for x in q3 if x != "b"]
print(lt3)

q6 = [x for x in range(1,101) if x%2 != 0]
print(q6)

