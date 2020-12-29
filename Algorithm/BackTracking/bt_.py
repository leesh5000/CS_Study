# Back Tracking
# - 백트래킹(혹은 퇴각검색)은 알고리즘은 아니고, 문제풀이전략
# - Constraint Satisfactory Problem 에서 해를 찾기 위한 전략
# - 백트래킹 대표 문제 : N-Queen 문제

def is_available(current_candidate, current_col):
    # 현재의 행은 candidate의 길이
    current_row = len(current_candidate)

    for queen_row in range(current_row):
        # current_candidate[queen_row]는 현재 퀸이 있는 열
        if current_candidate[queen_row] == current_col or abs(current_candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def dfs(N, current_row, current_candidate, result):
    # 현재 행이 체스판의 크기와 같아지면,
    if current_row == N:
        # result에다가 지금까지의 후보들을 저장, 뒤에 current_candidate.pop()에 영향받지 않기위해 얕은복사값 대입
        result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        # current_candidate에는 현재까지의 퀸의 배치정보
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            dfs(N, current_row+1, current_candidate, result)
            current_candidate.pop()
            
def solution(N):
    result = []
    dfs(N, 0, [], result)
    return result

print(solution(4))