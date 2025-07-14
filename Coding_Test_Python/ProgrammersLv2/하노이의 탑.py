def solution(n) :
    def move(s , m , d , n ) :
        if n == 1 :
            return [[s,d]]
        if n == 2 :
            return [[s,m], [s,d], [m,d]]
        if n == 3 :
            return [[s,d], [s,m], [d,m], [s,d], [m,s], [m,d], [s,d]]
        
        if  n >= 4 :
            return move(s,d,m,n-1) + [[s,d]] + move(m,s,d,n-1)
    return move(1,2,3,n)
    
