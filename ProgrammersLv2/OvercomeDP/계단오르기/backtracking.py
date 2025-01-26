# # num_of_stairs = int(input())
# # stairs = []
# # for num in range(num_of_stairs) :
# #     stairs.append(int(input()))
    
stairs = [ 10,20,15,25,10,20]


def dfs(idx, prev_idx, total, answer ) :
    if idx == len(stairs) -1:
        answer = max(answer, total)
        return answer
    elif idx > len(stairs) -1 :
        return False
    for i in (1,2) :
        if prev_idx + 1 != idx and (idx + 1) < len(stairs):
            answer = (dfs(idx+1, idx, total + stairs[idx+1], answer))
            
        if (idx + 2 ) < len(stairs) :
            answer = (dfs(idx+2, idx, total + stairs[idx+2], answer))
        
    return answer

result = 0
result = max(result, dfs(0,0,stairs[0], 0))
result = max(result, dfs(1,1,stairs[1], 0))
print(result)
