
def solution(blue, white ) :
    
    total_size = blue * white
    
    for i in range(1, int(total_size)**0.5 + 1) :
        
        j = total_size / i
        if j % 1 != 0 :
            continue
        
        if 2*i + 2 * j - 4 == total_size :
            return [j, i]