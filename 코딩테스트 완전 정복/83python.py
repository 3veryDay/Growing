def solution(people, limit) :
    
    # 무게가 작은 순으로 정렬
    people.sort()
    total_boat = 0
    current_boat_weight = 0 
    while people :
        current_boat_weight += people.pop()
        if people :
            if people[0] + current_boat_weight > limit :
                total_boat += 1
                current_boat_weight = 0
                continue;
            elif people[0] + current_boat_weight == limit :
                total_boat += 1
                people.pop(0)
                current_boat_weight = 0
            else:
                # people[0] + current_boat_weight < limit
                # 제일 몸무게가 적은 people과 제일 몸무게가 큰 people의 합이 limit 보다 작을 때
                while people :
                    if current_boat_weight + people[0]< limit :
                        current_boat_weight += people.pop(0)
                    else :
                        break;
                total_boat += 1
                current_boat_weight = 0
        else : return total_boat + 1
    return total_boat 


print(solution([2,2,2,2,3], 5))