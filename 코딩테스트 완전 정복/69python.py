def solution(keyinput, board) :
    
    move = { "up" : [0,1], "down" : [0,-1], "right" : [1,0], "left" : [-1,0]}
    
    start =[0,0]
    
    for key in keyinput :
        dx, dy = move[key]
        
        if abs(start[0] + dx) <= int(board[0]/2) and  abs(start[1] + dy) <= int(board[1]/2) :
            start = start[0] + dx, start[1] + dy
            
    return start