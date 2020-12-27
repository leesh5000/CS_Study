# Greedy Algorithm
# - 매순간 최적의 경우만 선택하여 최종값 구함
# - 최종결과가 최적에 가까운 값을 구할수는 있지만, 최적의 해라는 보장은 없음

# 탐욕알고리즘 문제 1번
# 값이 4720원일때 동전 4개로 동전의 수를 가장 적게 지불하는방법

# 해결방법
# - 큰 동전을 먼저해야 동전의 수가 적어지므로, 큰 동전을 먼저해서 탐욕알고리즘 실행

coins = [500, 100, 50, 1]

def min_coin(price: int, coins: list)->list:
    total_coin_count = 0
    # 가장 적게 내는 방법의 동전 조합
    ret_coins = {}
    # 먼저, 동전을 내림차순으로 정렬
    coins.sort(reverse=True)

    for coin in coins:
        # 예) 4720 // 5 = 9
        coin_num = price // coin
        total_coin_count += coin_num
        # 예) 4720 = 9 * 500
        price -= coin_num * coin
        ret_coins[coin] = coin_num
    
    return total_coin_count, ret_coins

print(min_coin(4720, coins))

