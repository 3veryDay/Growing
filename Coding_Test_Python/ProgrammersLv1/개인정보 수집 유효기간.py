def solution(today, terms, privacies):
    year, month, day = map(int, today.split('.' ) )
    today = day  + 28*month + 28*12*(year-2000)
    
    answer = []
    
    # term별로 유효기간 정리되어있는 dic
    dic = {}
    for t in terms :
        term, month = t.split()
        dic[term] = int(month)
        
        
    for idx, p in enumerate(privacies) :
        date, term = map(str, p.split())
        year, month, day = map(int, date.split('.' ) )
        date = day  + 28*month + 28*12*(year-2000)
        term_day = dic[term] * 28
        
        if date + term_day <= today :
            answer.append((idx) + 1)
        
    return answer
