def solution(string):
    
    list = [0] * 27
    
    for s in string :
        tmp = ord(s) - 97
        list[tmp] += 1
    string = ''
    for letter, ind in enumerate(list) :
        if ind != 0 :
            string += chr(letter+97)*ind
    return string


print(solution('hello'))