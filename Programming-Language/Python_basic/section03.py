# Section03
# 파이썬 가상환경 및 pip 활용법

# 외부 설치 패키지 테스트
import simplejson as json

test_dict = {'1':95, '4':77, '5':88, '2':10, '3':50}

# simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4*' '))

# 