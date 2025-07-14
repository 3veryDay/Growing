#defining hash function for string, with p and m
def polynomial_hash_function(str) :

    p = 31
    #bucket size m
    m = 1_000_000_007
    hash_value = 0
    
    for char in str :
        hash_value = (hash_value * p + ord(char))% m
    return hash_value


def solution(string_list, query_list) :
    hash_list = [ polynomial_hash_function(str) for str in string_list]
    
    result = []
    
    for query in query_list :
        query_hash = polynomial_hash_function(query)
        
        if query_hash in hash_list :
            result.append(True)
        else : result.append(False)