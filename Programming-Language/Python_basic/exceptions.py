# section10
# 파이썬 예외처리

# linter : 코드 스타일, 문법 체크

# 1. SyntaxError : 문법이 틀린 경우
# if True
#     pass

# 2. NameError : 참조변수가 없을때
# a = 10
# b = 15
# print(c)

# 3. ZeroDivisionError : 0 나누기 에러
# print(10/0)

# 4. IndexError : 인덱스 범위 오버
# x = [10, 20, 30]
# print(x[4])

# 5. KeyError
# dic = {'name': 'kim'}
# print(dic['hobby'])
# print(dic.get('hobby'))

# 6. AttributeError : 모듈, 클래스에 잘못된 속성 사용 시 예외
# class Test:
#     val1
#     val2
# t = Test()
# t.val3

# 7. ValueError : 참조값이 없을 때 발생
# x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# 8. FileNotFoundError
# f = open('test.txt', 'r')

# 9. TypeError
# x = [1, 2]
# y = (1, 2)
# print(x+y)

# EAFP 코딩 스타일
# 1. 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 2. 그 후 런타임 예외 발생시 예외처리 하기

# 예외처리 기본
# try
# - 예외가 발생할 가능성이 있는 코드 실행
# - 예외가 발생하면 except문으로 이동

# except
# - 예외가 발생할 경우 실행

# else
# - 예외가 발생하지 않은 경우 실행

# finally
# - 항상 실행되는 구문

# 예외처리1 - 예외가 예상될때
# name = ['lee', 'kim', 'park']

# try:
#     z = 'kim'
#     x = name.index(z)
#     print('{} found it! in name'.format(z))
# except ValueError:
#     print('not found it! - valueError')
# else:
#     print('ok!')

# 예외처리2 - 어떤 예외가 발생할지 모를때
# name = ['lee', 'kim', 'park']

# try:
#     z = 'kim'
#     x = name.index(z)
#     print('{} found it! in name'.format(z))
# except Exception:
#     print('not found it!')
# else:
#     print('ok!')

# # 예외처리3 - finally
# name = ['lee', 'kim', 'park']

# try:
#     z = 'kim'
#     x = name.index(z)
#     print('{} found it! in name'.format(z))
# except Exception:
#     print('not found it!')
# else:
#     print('else')
# finally:
#     print('finally')

# # 예외처리4 - 예외처리는 하지 않지만 무조건 수행되는 코딩패턴
# try:
#     print('Try')
# finally:
#     print('ok finally!')

# 예외처리5 - 예외를 계층적으로 처리
name = ['lee', 'kim', 'park']
try:
    z = 'kim'
    x = name.index(z)
    print('{} found it! in name'.format(z))
except ValueError as ve:
    print(ve)
except IndexError as ie:
    print(ie)
except Exception:
    print('Exception')
else:
    print('else')
finally:
    print('finally')

# 예외6 - 예외를 직접 발생
try:
    a = 'lee'
    if a == 'lee':
        print('ok')
    else:
        raise ValueError 
except ValueError:
    print('value error')
except Exception as f:
    print(f)
else:
    print('ok')