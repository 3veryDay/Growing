def solution(amount) :
    denominations = [1,10,50,100]
    denominations.sort(reverse=True)
    given_coins = []
    
    for coin in denominations :
        while amount - coin >= 0:
            given_coins.append(coin)
            amount -= coin
    return given_coins


print(solution(350))