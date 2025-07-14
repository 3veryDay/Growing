# 한시간 살짝 넘게 걸렸지만... ㅎㅎ 그래도 내 힘으로 풀었음!


def solution(seq, k) :
    front, back = 0,0
    total = seq[front]
    if k in seq :
        return [seq.index(k), seq.index(k)]
    answer = []
    answer_len = len(seq) + 1
    while back != len(seq) - 1
        if front == back and back == len(seq) -1 :
            break
        if total == k :
            if back - front + 1 < answer_len :
                answer = [front, back]
                answer_len = back - front + 1
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

# 코드 수정


def solution(seq, k) :
    front, back = 0,0
    total = seq[front]
    if k in seq :
        idx = seq.index(k)
        return [idx, idx]        # 불필요한 중복 함수 호출
    answer = []
    answer_len = float('inf')    # 직관적인 최소 비교 길이 가능
    while back <len(seq) :       # 불필요한 if 문 제거
        if total == k :
            if back - front + 1 < answer_len :
                answer = [front, back]
                answer_len = back - front + 1
            total -= seq[front]
            front += 1
            
                
        elif total < k :
            back += 1
            if back <len(seq) :    # 인덱스 에러 방지
                total += seq[back]
        else :         #total < k  # 불필요한 elif 제거, 차라리 #문으로 처리하자
            total -= seq[front]
            front += 1
    return answer
