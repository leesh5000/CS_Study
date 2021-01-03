def solution(n: int, k: int) -> int:
    lt = []
    for i in range(1,n):
        if n % i == 0:
            lt.append(i)
    lt.append(n)

    # k번째 작은 수 뽑기
    idx = k-1
    if len(lt) < idx:
        return -1
    else:
        return lt[idx]

with open('./PS/input.txt', 'r') as f:
    line = f.readline()
    while line:
        n, k = map(int ,line.split())
        print(solution(n,k))
        line = f.readline()