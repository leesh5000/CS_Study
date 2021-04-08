# section13-1
# 타이핑 게임 제작

import random
import time
import pygame  # 사운드 출력모듈
# pylint: disable=no-member를 치면 해결되요.
import sqlite3
import datetime

# DB 생성 & Auto Commit
conn = sqlite3.connect('./resource/records.db', isolation_level=None)

# Cursor 연결
cursor = conn.cursor()

# 테이블 생성
cursor.execute(
    "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")

words = []   # 영어단어 리스트
n = 1       # 게임 시도 횟수
cor_cnt = 0  # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

input()
input("Ready? Press Enter Key!")

start = time.time()

while n < 6:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("*Question # {}".format(n))
    print(q)    # 문제출력

    x = input()  # 타이핑입력

    print()

    # pygame
    pygame.init()
    pygame.mixer.init()

    if str(q).strip() == str(x).strip():
        print('Pass!')
        # 정답 소리 재생
        pygame.mixer.Sound('./sound/good.wav').play()
        cor_cnt += 1
    else:
        pygame.mixer.Sound('./sound/bad.wav').play()
        print('Wrong!')

    n += 1

end = time.time()   # Endtime 기록
tt = end - start    # total time
tt = format(tt, ".3f")

if cor_cnt > 2:
    print("합격")
else:
    print("불합격")

# 기록 DB 삽입
cursor.execute("INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)",
               (cor_cnt, tt, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

# 수행시간 출력
print("총 걸린 시간:", tt, "초", "정답 개수:{}".format(cor_cnt))

# 시작지점
if __name__ == '__main__':
    pass
