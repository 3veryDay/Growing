



''' ------------------------- '''
k = int(input())
value = '0'

def change(val1) :
    val2 = ''
    for v in val1 :
        if v == '1' :
            val2 += '0'
        else : 
            val2 += '1'
    return val2
while len(value) <= k :
    value += change(value)
print(value)
print(value[k-1])

'''-> 시간 초과'''
