#  주식을 사고 팔기 가장 좋은 시점
 
#  한번의 거래로 낼 수 있는 최대 이익을 산출하라
 
#  입력 [7,1,5,3,6,4]
 
#  출력 5
#  1일 때 사서, 6일 때 팔면 5의 이익을 얻는다.

def brute(nums) :
    answer = []
    for i in range(1, len(nums)) :
        buying_point = min(nums[:i])
        answer.append(nums[i] - buying_point)
        print(answer)
    return max(answer)

tmp = [7,1,5,3,6,4]
print(brute(tmp))