def solution(records):
    user = {}
    command = {}
    result = []
    command["Enter"] = "님이 들어왔습니다."
    command["Leave"] = "님이 나갔습니다."
    for record in records :
        line = record.split(' ')
        
        if line[0] == "Enter" or line[0] == "Change" :
            user[line[1]] = line[2]
    for record in records :
        line = record.split(' ')
        if line[0] != "Change" :
            result.append(user[line[1]] + command[line[0]])
        
    
    return result
