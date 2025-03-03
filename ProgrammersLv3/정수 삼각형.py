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

  ''' 효율성 0 '''
