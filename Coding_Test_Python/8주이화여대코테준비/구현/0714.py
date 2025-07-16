N = int(input())
dic = set()

for _ in range(N ) :
    typed = input()
    flag = 0
    answer =''
    for word in typed.split() :
        # print(word)
        if flag == 0 and word[0].lower() not in dic:
            dic.add(word[0].lower())
            flag = 1
            answer += "["+word[0] + "]" + ''.join(word[1:])
        else : answer += word
    if flag == 1 : print(answer)
    if flag == 0 :
        answer =''
        for idx, char in enumerate(typed) :
            if flag == 0 and char.lower() not in dic :
                dic.add(char)
                flag = 1
                answer += "["+char+"]"+ typed[idx+1:]
                break
            else : answer += char
        print(answer)