# 시간 복잡도 너무 높음
def solution(players, callings):
    answer = []
    for call in callings :
        idx = players.index(call)
        players[idx-1], players[idx] = players[idx], players[idx-1]
    
    return players
