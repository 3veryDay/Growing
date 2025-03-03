def solution(brown, yellow):
    tot = brown + yellow
    if int(tot**0.5) == tot**0.5 :
        t =int(tot**0.5) 
    else : t = int(tot**0.5) + 1
    for x in range(t ,  tot + 1 ) :
        if tot % x == 0 :
            y = tot // x
            print(x,y)
            if 2*(x+y)-4 == brown :
                return [x,y]
