#section12-1
# 파이썬 패키지에는 SQLite가 기본적으로 포함되어이다.

# 테이블 생성 및 삽입

import sqlite3
import datetime

print()

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

now_data_time = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_data_time)

print(sqlite3.version)
print(sqlite3.sqlite_version)

# DB생성 & Auto Commit 설정 , Rollback
conn = sqlite3.connect('./resource/database.db', isolation_level=None)

# Cursor 커서의 획득
c = conn.cursor()
print('Cursor Type:',type(c))

# 테이블 생성
# SQLite의 자료형
# - TEXT
# - Numeric
# - Integer
# - REAL
# - BLOB

c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")


# 데이터 삽입
# c.execute("INSERT INTO users VALUES(1, 'Lee', 'Lee@gmail.com', '010-6271-5427', 'Lee.com', ?)", (now_data_time,))
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'Kim', 'Kim@daum.net', '010-9739-5435', 'Kim.com', now_data_time))

# Many 삽입 - 한번에 대용량의 데이터를 삽입하는 방법 (튜플, 리스트)
user_list = (
    (3, 'Park', 'Park@naver.com', '010-0000-0000', 'Park.com', now_data_time),
    (4, 'Ko', 'Ko@naver.com', '010-1111-1111', 'Ko.com', now_data_time),
    (5, 'You', 'You@naver.com', '010-2222-2222', 'You.com', now_data_time),
)

# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", user_list)


# 데이터 삭제
# conn.execute("DELETE FROM users")
# print("users db deleted :", conn.execute("DELETE FROM users").rowcount)


# 커밋 : isolation_level==None 일 경우는 자동반영 (auto commit)
# auto commit이 아니면 conn.commit()
# 커밋을 취소하려면, conn.rollback()

# DB 접속 해제
# conn.close()

# 테이블 조회, 조건 조회
