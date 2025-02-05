def solution(n):
    #Bottom up
#     dp = [-1]*(n+ 1)
#     if n == 1 or n == 2 or n == 3 :
#         return n
    
#     for i in range(n+ 1) :
#         if i == 1 or i == 2 or i == 3 :
#             dp[i] = i
#         else :
#             dp[i] =  (dp [i-1] + dp[i-2] ) % 1000000007
#     return dp[n]
