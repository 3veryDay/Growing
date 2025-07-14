from collections import defaultdict


def solution(words) :
    
    words_dict = {}
    
    for word in words :
        
        if ''.join(sorted(word)) not in words_dict.keys() :
            words_dict[''.join(sorted(word)) ] = [word]
        else :
            words_dict[''.join(sorted(word)) ].append(word)
    result =list (words_dict.values())
    
    
    return result
    
    
a = [ "eat", "tea", "tan", "ate", "nat", "bat" ]
print(solution(a))