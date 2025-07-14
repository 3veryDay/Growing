def solution(input) :
    input.lower()
    value = True
    alpha_num_string = ""
    for char in input :
        if char.isalnum() :
            alpha_num_string += char
    print(alpha_num_string)
    for idx in range(len(alpha_num_string )) :
        if alpha_num_string[idx] != alpha_num_string[-idx-1] :
            value = False
        
    return value


print(solution(" a man a plan,, a canal : panama"))