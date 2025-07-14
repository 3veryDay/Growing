def solution(want, number, discount) :
    dict = {}
    cnt = 0
    for i in range(len(want)) :
        dict[want[i]] = number[i]
        
    
    for i in range(10):
        if discount[i] in dict :
            dict[discount[i]] -= 1

    
    for day in range(0, len(discount) - 9) :
        print(day, cnt, dict)
        if all(value == 0 for value in dict.values()):
            cnt += 1
            print("if",day, cnt, dict)
        
        
        if discount[day] in dict :
            dict[discount[day]] += 1
        
        if day+10 < len(discount) and discount[day+10] in dict : 
            dict[discount[day+10]] -= 1
    
    return cnt

print(solution(["banana", "apple", "rice", "pork", "pot"],	[3, 2, 2, 2, 1],	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))


for i in range(3) :
    print(i)