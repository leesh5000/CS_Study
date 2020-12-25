# 탐욕알고리즘 문제 2 - 부분배낭문제(Fractional Knapsack Problem)
# - 무게 제한이 K인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
# - v 가치를 갖는 물건은 쪼개서 배낭에 넣을 수 있음(Fractional)

# 패스트캠퍼스 탐욕알고리즘2번 강의보기

# (무게, 가치)
data_list = [(20, 10), (10, 10), (15, 12), (30, 5), (25, 8)]
# sorted 내장함수 사용 : key값이 가장 큰 것부터 맨 앞으로  (key값은 무게당가치)
# , reverse=True이니까, key(무게당가치)가 큰 값부터 정렬
data_list = sorted(data_list, key=lambda x: x[1]/x[0], reverse=True)

# 현 순간의 최적해(무게당가치가 가장 큰 값)부터 그리디알고리즘 실행
def max_value(data_list: list, capacity: int):
    # 먼저, 매개변수로 받은 리스트를 최대가치순으로 정렬
    data_list = sorted(data_list, key=lambda x: x[1]/x[0], reverse=True)
    # 전체가치
    total_value = 0
    # 최대 가치를 이루는 조합
    details = []

    for data in data_list:
        # 가방용량이 무게보다 더 크면, 그냥 통째로 넣기
        if capacity - data[0] >= 0:
            # 물건을 넣으면, 가방 용량에 물건 무게만큼 빼기
            capacity -= data[0]
            # 가방안의 전체 가치에 물건의 가치만큼 더하기
            total_value += data[1]
            # 물건을 가방에 넣었으니 전체 조합에 물건 추가 (무게, 가치, 몇%)
            details.append({'무게': data[0],'가치': data[1],'분할': 1})
        # 물건이 가방용량보다 크다면, 물건을 쪼개서 넣어야함
        else:
            # 만약, 가방의 남은용량 5이고, 물건의 무게가 10이라면, 5/10=0.5로 물건의 0.5만 넣어야됨
            fraction = capacity / data[0]
            capacity -= data[0] * fraction
            total_value += data[1] * fraction
            details.append({'무게': data[0],'가치': data[1],'분할': fraction})
            # 물건이 가방용량보다 크면, 여기서 물건을 분할해서 넣으면 더이상 다음 물건을 볼 필요없음
            break
    
    return total_value, details

data_list = [(20, 10), (10, 10), (15, 12), (30, 5), (25, 8)]
print(max_value(data_list, 30))