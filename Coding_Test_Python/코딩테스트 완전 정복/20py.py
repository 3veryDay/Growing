def polynomial_hash_function(str) :
    p = 31
    m = 1_000_000_007
    hash_value = 0
    
    for char in str :
        hash_value = (hash_value * p + ord(char))% m
    return hash_value

print(polynomial_hash_function("apple"))