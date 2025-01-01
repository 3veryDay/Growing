def solution(triangle) :
    dp = [[0]*len(row) for row in triangle]
    height = len(triangle)-1
    for j in range(len(triangle[height])) :
        dp[height][j] = triangle[height][j]
    print(dp)
    for i in range(height , 0, -1) :
        for j in range(len(triangle[i])-1 ):
            
            dp[i-1][j] = max(dp[i][j], dp[i][j+1]) + triangle[i-1][j]
        print(dp)
    return dp[0][0]
    
t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(t))