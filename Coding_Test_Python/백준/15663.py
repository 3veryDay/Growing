from collections import defaultdict

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
numbers_dic = defaultdict(int)
for num in numbers :
    numbers_dic[num] += 1

def backtrack(path, depth) :
    # 종료 조건
    if depth == M :
        print(*path)
        return
    
    # 후보군 탐색
    for nxt_num, cnt in numbers_dic.items() :
        if cnt > 0 :
            numbers_dic[nxt_num] -= 1
            path.append(nxt_num)
            backtrack(path, depth + 1)
            numbers_dic[nxt_num] += 1
            path.pop()
          
for start_num in numbers_dic.keys() :
    numbers_dic[start_num] -= 1
    backtrack([start_num], 1)
    numbers_dic[start_num] += 1
