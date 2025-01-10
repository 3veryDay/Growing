from collections import Counter


def solution(k, tangerine) :
    """귤 고르기
    
    한 상자에 담기는 귤의 개수 k와 귤의 크기가 담긴 배열 tangerine이 주어지면,
    크기가 서로 다른 종류의 수의 최솟값을 반환하는 함수수
    """
    tangerine_to_dict = dict(Counter(tangerine))
    print(tangerine_to_dict)
    dict_to_list = list(tangerine_to_dict.values())
    tangerine_num_list = sorted(dict_to_list ,reverse = True)
    
    index_of_tangerine = 0
    total_count = 0
    category_count = 0
    
    while index_of_tangerine <= len(tangerine) :
        if tangerine_num_list[index_of_tangerine] + total_count >= k :
            return category_count + 1
        
        # 총 개수가 k에 도달하지 않았을 경우
        total_count += tangerine_num_list[index_of_tangerine]
        category_count += 1
        index_of_tangerine += 1
        
    return category_count

print(solution(4 ,[1, 3, 2, 5, 4, 5, 2, 3]))
    
    
    
    