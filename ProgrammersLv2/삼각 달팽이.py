def solution(n):
    if n == 1:
        return [1]
    map = [ [0]* n for _ in range(n)]
    
    num = 1
    gar = 0
    sae = 0
    while num <= n*(n+1)/2 :
        
        while sae <= n-1 and map[sae][gar] == 0:
            map[sae][gar] = num
            sae += 1
            num += 1
        # print("1", map)
        sae -= 1
        gar += 1
        while gar <= n-1 and map[sae][gar] == 0 :
            map[sae][gar] = num
            gar += 1
            num += 1
        # print("2" , map)
        gar -= 2
        sae -= 1
        while map[sae][gar] == 0 :
            map[sae][gar] = num
            sae -= 1
            gar -= 1
            num += 1
        # print("3", map)
        # print(sae, gar)
        sae += 2
        gar += 1
    answer =[]
    for i in range(n) :
        for j in range(n) :
            if map[i][j] != 0 :
                answer.append(map[i][j])
            else :
                continue
            
    return answer
