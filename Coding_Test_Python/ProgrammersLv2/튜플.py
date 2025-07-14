def solution(s):
    s = list(s[2:-2].split("},{"))
    s.sort(key = lambda x : len(x))
    answer = []
    answer.append(int(s[0]))
    
    for string in s[1:] :
        for char in string.split(',')  :
            if int(char) not in answer :
                answer.append(int(char))
                continue
                
    
    return answer


#https://codechacha.com/ko/python-string-strip/

"""
lstrip에서 공백으로 전달하면 공백 제거지만,
인수 전달하면 그 인수가 안 보일 때까지 제거하고,
여러개의 인수가 전달되면, 거기에 없는 애가 나올 때까지 제거함.


"""
