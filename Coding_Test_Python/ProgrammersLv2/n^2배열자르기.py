#1차 시도, 정답은 맞으나 시간 초과
def solution(n, left, right):
    
    arr = []
    
    for i in range(1, (n+1)) :
        for I in range(i) :
            arr.append(i)
        tmp = i + 1
        while len(arr) % n != 0 :
            arr.append(tmp)
            tmp += 1
    return arr[left:right + 1]

#2차 시도 , 정답 (20분 안에 해결)
def solution(n, left, right) : 
    arr = []
    for position in range(left, right + 1) :
        
        hang = position // n + 1
        yeol = position % n + 1
        if hang >  yeol :
            arr.append(hang)
        else :
            arr.append(yeol)
    return arr

"""
내가 생각한 hang > yeol 이 조건은 결국 max로 항상 바꿀 수 있다. 
>, < 나오면 max를 생각하되, 굳이 고생할 필요는 없을 듯! 
조금 더 여유가 생기면 
for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)


def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

"""
