def solution(records) :
    result = []
    dict = {}
    printer = {'Enter': '님이 들어왔습니다.', 'Leave' : '님이 나갔습니다.'}
    
    for record in records :
    #record가 "Enter uid1234 Muzi"
        r = record.split()
    
        if r[0] == "Enter" :
            dict[r[1]] = r[2]
        
        #f r[0] == "Leave" :
    
        if r[0] == "Change" :
            dict[r[1]] = r[2]
            
    for record in records :
        if record.split(' ')[0] != 'Change' :
            result.append(dict[record.split(' ')[1]] + printer[record.split(' ')[0]])

    return result


tmp = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(tmp))