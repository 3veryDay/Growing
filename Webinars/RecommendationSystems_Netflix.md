- 공부하는 입장에서는 추천 시스템에 대해서 알 수 없지만,
- we can know possible methods to making recommendation system
- it is applicable in everyday activities.

### Should I watch This Movie?
- if my friends like this movie -> I might like this movie. : Collaborative Filtering
- many factors that connect to my preference, other movies similar to the factors, I might like. : Content Based Filtering
- other factors : we have many other factors, informations, lots of media reports. (External Factors)

Solving this problem is very complex. needs so much information to build a recommendation system. 


### A recommender system should know what user needs ?
Google Search's input is the limited text, but google tries to collect external information to get exactly what I need.
ex) "BANK" -> 내가 만약 최근에 hotel을 예약했으면 RiverBank, 아니면 금융 Bank... 이런 식으로 외부 정보가 필요함. 
Netflix needs to understand, 


### Simplest Answer using Collaborative, and Content Based.
we need data to predict. and we use data and define relationships. (user - item)
ex ) user1 -see-> Movie1, Movie3 (이런 간단한 관계) : 이런 정보를 가지고는 많은 걸 예측할 수 없음. 
ex 2 ) user1 -별점3-> Movie 4 : content based filtering 사용 가능 -> 이러한 숫자 based 관계는 matrix로 정의 가능
- 여기 사이에 있는 hidden pattern을 찾아서 prediction을 할 수 있다. (pattern이 없으면 random, 예측 불가)
- Content Based Filtering : 대상 영화랑 비슷한 평점을 가진 영화를 예측에 사용
- Collaborative Filtering : 비슷한 평점을 준 사용자를 예측에 사용

more complex patterns ...도 존재함. (평점 더하기)

movies have underlying features as (Comedy, Musical, Action,,,... or 
