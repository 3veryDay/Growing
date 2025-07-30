import heapq

N = int(input())
cards = []
for _ in range(N) :
    cards.append(int(input()))
    
heapq.heapify(cards)
answer = 0

# 카드가 하나로 합쳐질 때까지
while len(cards) > 1 :
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    
    answer += (card1 + card2)
    heapq.heappush(cards, (card1+card2))

print(answer)
