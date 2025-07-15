# '''

# '''

# N, M은 8이상 50 이하
N, M = map(int, input().split())
board = []
for _ in range(N) :
    board.append(list(input().strip()))

# N, M = 8, 8
# board = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'B', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

def find(y, x) :
    starts_with_W, starts_with_B = 0, 0
    for i in range(8) :
        for j in range(8) :
            block = board[y+i][x+j]
            if block == "W" :
                if (i+j) % 2 == 0 :
                    starts_with_B += 1
                else :
                    starts_with_W += 1
            if block == "B" :
                if (i+j) % 2 == 0 :
                    starts_with_W += 1
                else : 
                    starts_with_B += 1
    # print(starts_with_B, starts_with_W)
    return min(starts_with_B, starts_with_W)
answer = float('inf')
for y in range(N - 7) :
    for x in range(M - 7) : 
        answer = min(answer, find(y,x))
        
print(answer)
