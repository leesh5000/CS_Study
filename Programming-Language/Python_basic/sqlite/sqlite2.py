# section12-2
# 파이썬 데이터베이스 연동 SQLite

# 테이블 조회
import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('./resource/database.db')

# 커서 바인딩
c = conn.cursor()
print(type(c))

# 전체 데이터조회
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 행 선택
# print('One ->\n', c.fetchone())
# 지정 행 선택
# print('Three ->\n', c.fetchmany(size=3))
# 전체 행 선택
# print('All ->\n', c.fetchall())

# 커서가 이동
# print('All ->\n', c.fetchall())

print()

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 >', row)

# 순회2 (가장 많이 쓰임)
# for row in c.fetchall():
#     print('retrieve2 >', row)

# 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrieve3 >', row)

# Where Retrieve1 - 튜플로 조회
param1 = (3, )
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1',c.fetchone())
print('param1',c.fetchall())

# Where Retrieve2 - 정수로 조회
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('param2',c.fetchone())

# Where Retrieve3 - 딕셔너리로 조회
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
print('param3',c.fetchone())

# WHERE Retrieve4 - IN은 OR
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3,4))
print('param5', c.fetchall())

# WHERE Retrieve6 - 딕셔너리로 조회
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
print('param6', c.fetchall())


# Dump 출력 - 연동된 데이터베이스의 SQL들을 백업하는 것
# with문을 쓰면 자동으로 open, close를 해준다. conn, open 둘 다
with conn:
    with open('./resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')
