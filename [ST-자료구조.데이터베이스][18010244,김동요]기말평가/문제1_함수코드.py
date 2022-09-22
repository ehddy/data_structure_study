# 문제 1: 선형조사를 위한 linear_prob.py에 삭제 연산을 위한 delete() 메소드를 추가하시오

'''저는 처음에 삭제된 원소를 None으로 바꿔 주었지만, 나중에 탐색 연산을 했을 때, 해당 해시 값이 None이면 조건에 따라
탐색 자체를 실패하는 문제가 있었습니다. 그래서 삭제할 원소를 None이 아닌 <delete>로 변경해주어 탐색을 원할하게 할 수 있도록 만들어 주었습니다. 
하지만, 삭제한 원소의 값을 <delete>로 바꾸면, 나중에 새로운 키의 삽입을 진행할 때, None이 아니기 떄문에, 해당 자리에 삽입을 안하는 문제가 
발생했습니다. 그래서 기존의 삽입 함수에 새로운 조건(self.a[i] == None or self.a[i] == '<delete>': 삽입 진행)을 추가해주어서 만약 해당 
리스트의 값이 None이거나 <delete>인 경우 그 자리에 새로운 키를 저장할 수 있도록 만들어 주었습니다. 또한, 삭제할 key의 인덱스만 반환해주는 함수(get_index)를 새로 만들어 주어서, 
삭제를 원할하게 진행했습니다. 
좀 더, 구체적인 내용 해당 함수의 주석을 달아놓았습니다  '''



class LinearProbing: # 선형 조사 
    def __init__(self, size):
        self.M = size # 테이블 크기
        self.a = [None] * size # 해시테이블 a 
        self.d = [None] * size # 데이터 저장용 d 

    def hash(self, key):
        return key % self.M # 나눗셈 해시함수

    
    def put(self, key, data): # 삽입연산
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        j = 0
        while True:
            #  None인 자리에만 값을 넣어주는 문제를 해결하기 위해, '<delete>'을 발견하면 값을 넣어 주는 조건을 추가  
            if self.a[i] == None or self.a[i] == '<delete>': # 빈곳 발견 
                self.a[i] = key # 키는 해시테이블에 data는 리스트 d에 저장 
                self.d[i] = data 
                return
            
            if self.a[i] == key: # key가 이미 해시테이블에 있으므로 data만 갱신 
                self.d[i] = data
                return  
            j += 1 
            i = (initial_position + j) % self.M
            if i == initial_position:
                break # 다음 위치가 초기 위치와 같으면 루프 벗어나기 [저장 실패]
        
    def delete(self, key):
        # 삭제할 key의 인덱스만 반환해주는 함수를 새로 만들어 주었다. 
        idx = self.get_index(key)
        # 반환 한 index(i)를 이용하여 값들을 제거해줌 
        # 해시 테이블의 해시 값(인덱스)를 <delete>로 바꿔주고, data는 None으로 바꿔준다. 
        self.a[idx] = '<delete>'
        self.d[idx] = None


    def get(self, key): # 탐색연산 
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i] # 탐색 성공
                
            i = (initial_position + j) % self.M #다음 원소 검사를 위해 
            j += 1      
            if i == initial_position:
                return None # 탐색 실패 
        # 탐색 실패 
        return None 

    # 삭제할 key의 인덱스만 반환해주는 함수를 새로 만들어 주었다.
    def get_index(self, key): # 탐색하려는 키의 인덱스를 반환하는 함수  
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return i # 탐색 성공
                
            i = (initial_position + j) % self.M #다음 원소 검사를 위해 
            j += 1 
            if i == initial_position:
                return None # 탐색 실패 
        return None 
        
    def print_table(self): # 해시 테이블 출력 
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
        print()