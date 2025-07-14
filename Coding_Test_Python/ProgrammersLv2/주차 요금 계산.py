from collections import defaultdict
def solution(f, records):
    basic_time, basic_fee, per_min, price = f
    c = []
    
    def calculate(time) :
        #all given in min base
        if time <= basic_time :
            print(f'calculate - > if {basic_fee}')
            return basic_fee
        else :
            if ((time-basic_time)/per_min) % 1 != 0 :
                return (basic_fee + ((int((time-basic_time)/per_min)+1)* price))
            else :
                return (basic_fee + ((time-basic_time)//per_min)*price)
        
        
    dic = {}
    sum_ =defaultdict(int)
    for record in records :
        time, car, in_out = record.split()
        if car not in c :
            c.append(car)
        h, m = map(int, time.split(':'))
        time = 60*h + m 
        if in_out == 'IN' :
            dic[car] = time
        else :       # OUT
            sum_[car] += ( time - dic.pop(car) )
            print("여기!",car,  sum_[car])
    
    #아직 안 나간 차에 대한 계산
    tmp = list(dic.keys())
    if tmp :
        for t in tmp :
            sum_[t] += ((23*60 + 59) - dic.pop(t))
            
    answer = []
    c.sort()
    for car in c :
        print(car, (sum_[car]))
        answer.append(calculate(sum_[car]))
        
    return answer
