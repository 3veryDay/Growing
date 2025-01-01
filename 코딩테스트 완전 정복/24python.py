def solution(id_list, reports, k) :
    people_dict = {}
    num_dict = {}
    
    over_k = []
    result = []
    for report in reports :
        print(report)
        print(people_dict, num_dict)
        reporter = report.split(' ')[0]
        reported = report.split(' ')[1]
        if reporter in people_dict: 
            if people_dict[reporter] == [reported] :
                print("continue")
                continue;
        elif reporter not in people_dict :
            people_dict[reporter] = []
            print("elif reporter not in people_dict :")
        if reported not in num_dict :
            num_dict[reported] = 0
            print("if reported not in num_dict")
        people_dict[reporter].append(reported)
        num_dict[reported] += 1
        
    for name, num in num_dict.items() :
        if num >= k :
            over_k.append(name)
    over_k = set(over_k)
    
    for name in id_list :
        print(name)
        cnt = 0
        if name in people_dict :
            
            report = people_dict[name]
            print(report)
            for id in report :
                print(id)
                if id in over_k :
                    cnt += 1
            result.append(cnt)
        else : result.append(0)
        
    return result
    
id_list =["muzi", "neo"]
reports = ["muzi neo","muzi neo","muzi neo","muzi neo"]
k = 2 
print(solution(id_list, reports, k))