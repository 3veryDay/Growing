#1:10 - 2 : 10
from collections import defaultdict


def solution(want, number, discount):
    """
    정현이가 원하는 제품을 나타내는 문자열 배열 : want
    정현이가 원하는 제품의 수량을 나타내는 정수 배열 : number
    마트에서 할인하는 제품을 나타내는 문자열 배열 : discount 
    
    -> 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원 등록 날짜의 총 일수
    없으면 0 반환
    
    """
    #shopping list의 key에는 원하는 제품, value에는 제품의 수량
    shopping_list = defaultdict()
    for i in range(len(want)) :
        shopping_list[want[i]] = number[i]
        
    sum_of_shopping_list = sum(number)
    cnt = 0
    
    for i in range(sum_of_shopping_list) :
        if discount[i] in shopping_list :
            shopping_list[discount[i]] -= 1
        else :
            shopping_list[discount[i]] = -1
            
    if set(shopping_list.values()) == 0:
        cnt += 1

    
    for i in range(len(discount) - sum_of_shopping_list) :
        j = i + sum_of_shopping_list
        
        if discount[i] in shopping_list :
            shopping_list[discount[i]] += 1
        else :
            shopping_list[discount[i]] = 1
            
            
        if discount[j] in shopping_list :
            shopping_list[discount[j]] -= 1
        else :
            shopping_list[discount[j]] = -1
        
        
        if set(shopping_list.values()) == {0}:
            cnt += 1
    
    
    return cnt
    
print(solution(["banana", "apple", "rice", "pork", "pot"]	,[3, 2, 2, 2, 1]	,["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))