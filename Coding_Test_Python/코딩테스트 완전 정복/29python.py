def solution(enroll, referall, seller, amount) :
    N = len(enroll)
    res = [0] * N
    # enroll_hash = {}
    # referall_hash = 
    # for i in N :
    #     enroll_hash[i] = enroll[i]
    #     referall_hash[i] = referall[i]
    enroll_map = {value: idx for idx, value in enumerate(enroll)} 
    referall_map = {value: idx for idx, value in enumerate(referall)} 

    for name, amount in zip(seller, amount) :
        amount *= 100
        tmp_name = name
        tmp_amount = amount
        while True :
            
            idx_of_name = enroll_map[tmp_name]
            ref = referall[idx_of_name]
            idx_of_ref = referall_map[ref]
            b = tmp_amount // 10
            a= tmp_amount - b
            print(res)
            if ref == '-' :
                print(name)
                if tmp_amount < 10 :
                    res[idx_of_name] += int(tmp_amount)
                else:
                    res[idx_of_name] += int(a)
                break;
            elif tmp_amount < 10 :
                print(name)
                res[idx_of_name] += tmp_amount
                break;
            else:
                res[idx_of_name] += int(a)
                print(name, "else")
                tmp_name = ref
                tmp_amount = b
    return res
    
enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	
referall = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	
seller = ["sam", "emily", "jaimie", "edward"]	
amount = [2, 3, 5, 4]
    
print(solution(enroll, referall, seller, amount))