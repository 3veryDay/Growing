n,m = map(int, input().split())

#하나의 수를 가지고 여러개의 소수가 아닌 친구들을 걸러내볼까?
lst = [0] * (m+1)
lst[0], lst[1]= -1,-1
for idx in range(2, m+1) :
    #idx는 2,3,4,5.... m+1
    if lst[idx] == 1 :
        continue;
    #일단 처음 들어온 2부터 처리
    if lst[idx] == 0 :
        # print on result
        if n <= idx <=m:
            print(idx)
        i=1
        while i*idx <= m :
            lst[i*idx] = 1
            i+=1


n,m = map(int, input().split())

#하나의 수를 가지고 여러개의 소수가 아닌 친구들을 걸러내볼까?
lst = [0] * (m+1)
lst[0], lst[1]= -1,-1
for idx in range(2, m+1) :
    #idx는 2,3,4,5.... m+1
    if lst[idx] == 1 :
        continue;
    #일단 처음 들어온 2부터 처리
    if lst[idx] == 0 :
        # print on result
        if n <= idx <=m:
            print(idx)
        i=idx
       #제곱부터 처리해도 충분해!!!
      '''
      2의 배수를 처리하면서 2*5
      3의 배수를 처리하면서 3*5
      4의 배수를 처리하면서 4*5 를 소수 아님으로 정리했기 때문애

      5일떄는 5*5(자기자신) 부터 시작하는게 이상적이야.

      근데 시간 복잡도는 그렇게 차이가 나지는 않아. 
      '''
        while i*idx <= m :
            lst[i*idx] = 1
            i+=1



n,m = map(int, input().split())

#하나의 수를 가지고 여러개의 소수가 아닌 친구들을 걸러내볼까?
lst = [0] * (m+1)
lst[0], lst[1]= -1,-1
answer = []
for idx in range(2, int(m**0.5) + 1) :
    #충격, 왜냐하면
    '''
    m = 20이라고 가정하면
    int(m**0.5) + 1 = 5야
    그러면 5*5 는 m 이상이잖아! 
    사실 5*4 이런 친구들은 
    idx가 4일때 다 처리됐을 거거든.
    
    그렇기에 in(m**0.5) + 1 = 5부터는 의미가 없어!! 
    아래에서 코드 작성했듯이, i = idx, 로 들어가고 그러면 lst[idx*idx] 부터 보는건데,
    이미 그건 m 보다 크니까!!!!
    '''
    if lst[idx] == 1 :
        continue;
    
    else :
        i=idx
        while i*idx <= m :
            lst[i*idx] = 1
            i+=1
            
            
for idx, val in enumerate(lst) :
    if val == 0 and idx >=n :
        print(idx)
        
