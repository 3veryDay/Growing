logs = ["dig1 8 1 51 " , "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

#dig1은 식별자, 순서에 영향을 끼치지 않지만, 뒤에 오는 문자가 동일하면 식별자 순으로 한다.

#숫자 로그는 입력 순서대로. 즉, 숫자는 크고 작음을 따지지 않는다

# 문자로 구성된 로그가 앞에 온다.

def solution( logs ) :
    
    logs_with_num = []
    logs_with_alpha = []
    #하나하나 분리
    #숫자가 포함된 log은 순서대로 logs_with_num 배열에 추가
    for log in logs :
        word = log.split(' ')
        if word[1].isalpha() :
            logs_with_alpha.append(log)
        else :
            logs_with_num.append(log)
    print(logs_with_alpha, logs_with_num)
            
    logs_with_alpha.sort(key = lambda x : (x.split(' ')[1], x.split(' ')[0] ))
    answer = []
    answer += logs_with_alpha + logs_with_num
    print(answer)
    
solution(logs)
    
    
        