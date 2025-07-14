def solution(n,k,cmd) :
    ind = k
    answer = ['O'] * n
    stacked = []
    for c in cmd :
        movement = c[0]
        #movement 는 D, U, C, Z 중 하나
        if movement == 'D' :
            #움직일 숫자
            cnt = int(c[2])
            while cnt >0:
                if answer[ind] == 'O' :
                    ind +=1
                else :  #answer[ind] == 'X'
                    ind +=2
                cnt -=1
            
        
        if movement == 'U' :
            
            #움직일 숫자
            cnt = int(c[2])
            while cnt > 0:
                if answer[ind] == 'O' :
                    ind -=1
                else :  #answer[ind] == 'X'
                    ind -=2
                cnt -=1
            
        if movement == 'C' :
            answer[ind] = 'X'
            stacked.append(ind)
            if ind == n-1 :
                ind -=1
            else : ind += 1
            
        if movement == 'Z' :
            if stacked :
                tmp = stacked.pop()
                answer[tmp] = 'O'
                
        print(c, "   ", ind)
        print(answer)
            
            
            
            
            
    return ''.join(answer)

print(solution(8,2,[ "D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))

print(solution(8,2,[ "D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
