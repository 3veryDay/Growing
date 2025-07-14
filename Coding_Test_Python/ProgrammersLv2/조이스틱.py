def solution(name):
    #65 ->'A' (ascii(숫자)), 'A'->65 ord(알파벳) Z->90, J=74
    tmp = 65
    count = 0
    for idx, char in enumerate(name) :
        if idx >0 and name[idx] == name[idx-1] :
            count += 1
            continue
        tmp = abs(ord(char) - tmp)
        if tmp > 13 :
            tmp = 26 - tmp
        count += tmp
        
        # abcdefghijklmnopqrstuvwxyz
        print(f'char : {char},tmp:{tmp},  count:{count}')
        
        tmp = ord(char)
        count += 1
            
    return count - 2
