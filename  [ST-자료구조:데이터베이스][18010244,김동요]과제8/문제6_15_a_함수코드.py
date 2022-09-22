class LinearProbing: # 선형 조사 
    def __init__(self, size):
        self.M = size # 테이블 크기
        self.a = [None] * size # 해쉬테이블 a 
        self.d = [None] * size # 데이터 저장용 d 

    def hash(self, key):
        return key % self.M # 나눗셈 해시함수

    
    def put(self, key, data): # 삽입연산
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None: # 빈곳 발견 
                self.a[i] = key # 키는 해쉬테이블에 data는 리스트 d에 저장 
                self.d[i] = data 
                return
            
            if self.a[i] == key: # key가 이미 해시테이블에 있으므로 data만 갱신 
                self.d[i] = data
                return
            j += 1 
            i = (initial_position + j) % self.M
            if i == initial_position:
                break # 다음 위치가 초기 위치와 같으면 루프 벗어나기 [저장 실패]

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
        return None 

    def print_table(self): # 해쉬 테이블 출력 
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
                
        print()