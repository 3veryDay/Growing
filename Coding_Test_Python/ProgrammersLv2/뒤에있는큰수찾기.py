#30분 경과
def solution(num) :
    dp = [-1] * len(num)
    
    for idx in reversed(range( len(num)-1)) :
        
        if num[idx] >= num[idx + 1] and num[idx] <= dp[idx + 1] :
            dp[idx] = dp[idx + 1]
        elif num[idx] >= num[idx + 1] and num[idx] > dp[idx + 1] :
            for compare in num[idx + 1 :] :
                if num[idx] < compare :
                    dp[idx] = compare
                    break
        else :
            dp[idx] = num[idx + 1]
        
    return dp

#답
from collections import deque

def solution(num):
    n = len(num)
    dp = [-1] * n  # 정답 배열 (-1로 초기화)
    dq = deque()  # 사용할 deque (monotonic queue)

    for i in range(n - 1, -1, -1):  # 뒤에서부터 탐색
        # 현재 값보다 작은 값들은 큐에서 제거 (우리는 큰 값만 필요)
        while dq and dq[0] <= num[i]:
            dq.popleft()
        
        # dp 갱신: 남아있는 값 중 가장 앞에 있는 것이 우리가 찾는 값
        if dq:
            dp[i] = dq[0]
        
        # 현재 값을 큐에 추가
        dq.appendleft(num[i])

    return dp
