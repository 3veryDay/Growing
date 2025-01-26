
def TopDown(num ) :
    if num <= 3 :
        return 1
    dp = [-1 for _ in range(num + 1)]
    dp[1] , dp[2], dp[3] = 1,1,1
    def tmp(i) :
        if dp[i] != -1 :
            return dp[i]
        
        if i%3 == 0 and i %2 == 0:
            dp[i] = min(tmp(i//3), tmp(i//2), tmp(i-1))
        elif i%3 == 0 and i% 2 != 0 :
            dp[i] = min(tmp(i//3), tmp(i-1)) + 1
        elif i%3 != 0 and i % 2 == 0 :
            dp[i] = min(tmp(i-1), tmp(i//2)) + 1
        else:
            dp[i] = tmp(i-1) + 1
        return dp[i]
    return tmp(num)
print(TopDown(10))


