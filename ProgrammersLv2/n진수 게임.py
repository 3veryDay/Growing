'''
TypeError: can only concatenate str (not "int") to str
이건 int 와 str을 더하려고 할 때 나는 오류
'''

def solution(n, t, m, p):
    dict = {}
    dict[10],dict[11],dict[12],dict[13],dict[14],dict[15] = 'A', 'B', 'C', 'D', 'E', 'F'
    def change_n(num: int , n : int ) -> str :
        if num == 0 :
            return 0
        tmp = []
        while num > 0 :
            leftover = num % n 
            if leftover >= 10 :
                tmp.append(dict[int(leftover)])
            else :
                tmp.append(str(num % n))
            num = num // n      
        return ''.join(tmp[::-1])
    
    say = ''
    num = 0
    while len(say) < t * m :
        say += str(change_n(num, n))
        num += 1
    answer =''
    for idx in range(t) :
        answer += say[idx*m + (p-1)]
    
    return answer
