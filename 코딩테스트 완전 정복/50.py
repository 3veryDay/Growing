# def solution(n) :
#     answer_cnt = 0
#     def check_answer(a, y, hori, top_left, top_right, answer_cnt ) :
        
        
#         if a in hori or a-y in top_left or a+y in top_right :
#             return
#         else :
#             hori.add(a)
#             top_left.add(a-y)
#             top_right.add(a+y)

#         if y == (n-1) :
#             answer_cnt += 1
#             return answer_cnt
#         else :
#             return y
                
#     for queen_first_line in range( n ) :
#         hori = set()
#         hori.add(queen_first_line)
        
#         top_left = set()
#         top_left.add(queen_first_line - 0)
        
#         top_right = set()
#         top_right.add(queen_first_line + 0)
        
#         y_value = 1
#         while y_value <= n-1 :
#             print(hori, top_left, top_right)
#             for a in range(n) :
#                 if a not in hori:
#                     check_answer(a, y_value, hori, top_left, top_right, answer_cnt )
#             y_value += 1
#     return answer_cnt        

# print(solution(4))


def check( n, y, width, top_left, top_right, ans ) :
    ans = 0
    if y == n :
        ans += 1
    else : 
        
        
        for i in range(n) :
            if width[i] or top_left[i - y + n] or top_right[i + y] :
                #3 중 하나라도 False면 백트래킹
                continue
            
            width[i]= top_left[i - y + n] =  top_right[i+y] = True
            ans += check(n, y+1, width, top_left, top_right, ans)
            width[i] = top_left[i - y + n] =top_right[i+y] = False
            
    return ans

def solution(n) :
    ans = 0
    ans = check(n, 0, [False]*( n ), [False]*(n * 2), [False]*(n * 2) , 0)
    return ans

print(solution(4))    