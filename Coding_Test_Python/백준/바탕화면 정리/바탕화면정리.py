def solution(wallpaper):
    
    h, w = len(wallpaper), len(wallpaper[0])
    lux, luy ,rdx, rdy =w,h, 0,0 
    for y in range(h) :
        for x in range(w) :
            if wallpaper[y][x] == "#" :
                if lux > x:
                    lux = x
                if luy > y:
                    luy = y
                if rdx < x: 
                    rdx = x
                if rdy < y:
                    rdy = y
            # print(luy, lux, rdy+1, rdx+1)
                
                
    
    
    
    answer = [luy, lux, rdy+1, rdx+1]
    return answer
