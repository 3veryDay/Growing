def solution(s):
    answer = []
    
    def  change( s ) :
        tmp = s.count('1') # tmp는 int
        
        zero = len(s) - tmp # zero도 int
        ans = ''            # ans는 str
        # while tmp != 0 :
        #     ans += str(tmp % 2)
        #     tmp //= 2
        # return [(zero), ans[::-1]]
        return [zero, bin(tmp)] 
      

    answer = [0,0]
    while s != '1':
        z, s = change(s)
        answer[1] += (z)
        answer[0] += 1
        
    
    return answer
