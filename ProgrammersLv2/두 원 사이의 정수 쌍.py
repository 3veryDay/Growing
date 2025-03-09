import math
def solution(r1, r2):
    answer = 0
    #ValueError: math domain error : sqrt 안에 들어간 수가 음수일 때. 
    for x in range(1, r2) :
        #해당 x 좌표에 r1 원과 r2 원이 각각 y좌표가 어디있는지. 
        r1_y = (math.sqrt(max(1, r1**2 - x**2)) ) 
        r2_y = (math.sqrt(max(1, r2**2 - x**2)) )
        
        if r1_y % 1 == 0 :
            answer += int(r2_y)+1-r1_y
            # print("A", int(r2_y)+1-r1_y)
        elif r2_y %1 == 0 :
            answer += r2_y - int(r1_y)
            # print("B",  r2_y - int(r1_y))
        else :
            answer += int(r2_y) - int(r1_y)
            # print("C", int(r2_y) - int(r1_y))
    
    
    answer *= 4
    answer += 4*(r2-r1+1)
    return answer
