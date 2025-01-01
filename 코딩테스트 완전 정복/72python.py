def solution(arr) :
    N = len(arr[0])
    
    dp = [[0 for _ in range(N+1)] for _ in range(4+1)]
    
    for horizontol in range(1,N+1) :
        h = horizontol
        choices = [arr[0][h-1], arr[1][h-1], arr[2][h-1], arr[0][h-1] + arr[2][h-1] ]
        
        for k, choice in enumerate(choices) :
            k += 1
            #k는 1,2,3,4 choice는 더하기의 결과
            
            if k == 1 :
                dp[k][h] = max( dp[2][h-1], dp[3][h-1]) + choice
            elif k == 2 :
                dp[k][h] = max( dp[1][h-1], dp[3][h-1], dp[4][h-1]) + choice
            elif k == 3 :
                dp[k][h] = max( dp[1][h-1], dp[2][h-1]) + choice                
            elif k == 4 :
                dp[k][h] = dp[2][h-1]+ choice
                
            print(dp[0][h], dp[1][h], dp[2][h], dp[3][h], dp[4][h])
                
            
    
    
    return dp[4][N]
    
test_arr = [ [1,3,3,2],  [2,1,4,1], [1,5,2,3]]
test_arr = [[1,7,13,2,6], [1,-4,2,5,4], [5,3,5,-3,1]]
print(solution(test_arr))    