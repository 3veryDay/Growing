#1차 시도, 근데 testcase 9만이 안됨. 그래서 힌트가 있었나봄.! 
#이건 알고리즘 생각 하나도 안 하고, 시간 복잡도 보려고 한건데, 이것도 괜찮나
def solution(cite):
    answer = 0
    for i in reversed(range(len(cite))) :
        count = 0
        for num in cite :
            if num >= i :
                count += 1
            if count > i :
                count = 0
                break;
        answer= max(answer, count )
        
    return answer
        
        
