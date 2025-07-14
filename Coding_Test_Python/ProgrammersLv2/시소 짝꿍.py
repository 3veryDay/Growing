from collections import Counter
def solution(w) :
    w.sort()
    dic = dict(Counter(w))
    print(dic)
    answer = 0
    for val in dic.keys() :
        if dic[val] ==2 :
            answer += 1
        elif dic[val] > 2 :
            answer += (dic[val]-1)*(dic[val])//2
        
        
        if val*2 in dic.keys() :
            answer += dic[val] * dic[val*2]
        if val*3/2 % 1 == 0 and int(val*3/2) in dic.keys() :
            print(val, val*3/2)
            answer += dic[val] * dic[int(val*3/2)]
        if val*4/3 % 1 == 0 and int(val*4/3) in dic.keys() :
            print(val, val*4/3 )
            answer += dic[val] * dic[int(val*4/3)]
    return answer
