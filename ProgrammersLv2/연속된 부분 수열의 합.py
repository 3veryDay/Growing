# 한시간 살짝 넘게 걸렸지만... ㅎㅎ 그래도 내 힘으로 풀었음!


def solution(seq, k) :
    front, back = 0,0
    total = seq[front]
    if k in seq :
        return [seq.index(k), seq.index(k)]
    answer = []
    answer_len = len(seq) + 1
    while True :
        if front == back and back == len(seq) -1 :
            break
        if total == k :
            # print(front, back)
            if back - front + 1 < answer_len :
                answer = [front, back]
                # print(front, back)
                answer_len = back - front + 1
                # print("A", answer_len, answer)
            if back == len(seq) -1 :
                break;
            total -= seq[front]
            front += 1
            back += 1
            total += seq[back]
            
                
        elif total < k :
            if back == len(seq) -1 :
                break
            back += 1
            total += seq[back]
        elif total > k :
            if front == len(seq) -1  :
                break
            total -= seq[front]
            front += 1
    return answer
            
