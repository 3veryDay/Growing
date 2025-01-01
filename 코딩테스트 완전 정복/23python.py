def solution(genres, plays) :
    genres_dict = {}
    plays_dict = {}
    answer = []
    
    for i in range(len(genres)) :
        genre = genres[i]
        play = plays[i]
        
        if genre not in genres_dict :
            genres_dict[genre] = []
            plays_dict[genre]=0
        genres_dict[genre].append((i, play))
        plays_dict[genre] += play
        
    sorted_plays = sorted(plays_dict.items(), key=lambda x: x[1], reverse=True)
    for play, _ in sorted_plays :
        #play는 pop, classic
        sorted_genres = sorted(genres_dict[play], key = lambda x : x[1], reverse=True)
        
        answer.extend([idx for idx, _ in sorted_genres[:2]])
    
        
        
    return answer
genres =     ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
        