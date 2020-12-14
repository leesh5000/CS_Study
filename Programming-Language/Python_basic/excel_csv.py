# section11

# 파이썬 외부파일 처리
# csv : mime - text/csv

# # ex1
import csv
with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f)
    # next(reader) - csv table Header 스킵하기
    print(reader)
    print(type(reader))
    print(dir(reader))
    
    for c in reader:
        print(c)

# ex2 - 구분자 사용 delimiter
with open('./resource/sample2.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f, delimiter='|')
    # next(reader) - csv table Header 스킵하기
    print(reader)
    print(type(reader))
    print(dir(reader))
    
    for c in reader:
        print(c)

# 예제3 - Dict 변환
with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.DictReader(f)

    for c in reader:
        print(c)
        for k, v in c.items():
            print(k,v)
        print('-----------')

# ex4 - csv 쓰기, 한줄씩
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    for v in w:
        wt.writerow(v)

# ex5 - for문 없이 쓰기
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)

# 엑셀(XSL, XLSX)
# - XSL은 이전 버전
# - 엑셀처리 라이브러리 : openpyxl, xlsxwriter, xlrd, xlwt, xlutils, ...
# - pandas를 사용한다(pandas는 openpyxl, xlrd를 사용)
# - pandas는 데이터조작과 분석을 위한 파이썬 라이브러리
# - pip install xlrd
# - pip install openpyxl
# - pip install pandas

import pandas as pd

# sheetname = '시트명' 또는 숫자, header=숫자, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx', engine='openpyxl')

print(xlsx.head())
print(xlsx.tail())
print(xlsx.shape) # 행, 열의 수

# 엑셀 or CSV 다시쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)