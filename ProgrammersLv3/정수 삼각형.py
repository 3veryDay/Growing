def solution(triangle):
    idx = 0
    q = []
    dp = [[-1]*len(triangle[i]) for i in range(len(triangle))]
    q.append([0, 0, 0])
    answer = 0
    # for i in range(len(triangle)) :
    #     for j in range(len(triangle[i])) :
    #         print(triangle[i][j])
    while q :
        # 꺼내지면서 방문
        level, idx, total = q.pop()
        total += triangle[level][idx]
        # 종료 조건
        if level == len(triangle)-1 :
            if answer < total :
                answer = total
            continue
        if dp[level][idx] >= total :
            continue
        if dp[level][idx] == -1 or dp[level][idx] < total :
            dp[level][idx] = total
            q.append([level + 1, idx , total])
            q.append([level + 1, idx+1 , total])
    return answer
'''

dP로 갈라치기를 한다고 해서 효율적인게 아니다. 
q에서 넣고, 빼는 것이 효율적이지 않다.
이 방식은 최적의 경로를 찾을 때 탐색해야 할 경우의 수가 너무 많아 성능이 좋지 않음.

DP는 bottom-up 방식과, top-down 방식이 있음. 
dp를 했는데, bottom up이 잘 안 먹힌다면, top down을 시도해볼 필요가 있다. 
'''
  ''' 효율성 upgrade '''
def solution(triangle) :
    bottom = len(triangle) - 1
    bottom_idx = len(triangle[bottom])
    dp = [[0]*len(triangle[idx]) for idx in range(len(triangle))]
    for last_level in range(0, bottom_idx) :
        dp[bottom][last_level] = triangle[bottom][last_level] 
    for level in range(bottom-1, -1, -1) :
        for idx in range(len(triangle[level])) :
            dp[level][idx] = max(dp[level+1][idx] , dp[level+1][idx+1]) + triangle[level][idx]
    return dp[0][0]


def solution(triangle) :
    bottom = len(triangle) - 1
    bottom_idx = len(triangle[bottom])
    for level in range(bottom-1, -1, -1) :
        for idx in range(len(triangle[level])) :
            triangle[level][idx] = max(triangle[level+1][idx] , triangle[level+1][idx+1]) + triangle[level][idx]
    return triangle[0][0]
