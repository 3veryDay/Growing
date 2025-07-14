
N = int(input())
board = []
for _ in range(N):
    start, end = map(int, input().split())
    time = end-start
    board.append([start, end, time])
    
board.sort(key = lambda x : ([x[1], x[0], x[2]]))
# print(board)
count = 1
now = board[0][1]

for t in board[1:] :
    start, end, time = t
    
    if start >= now :
        now = end
        count += 1
        # print(t)
print(count)
