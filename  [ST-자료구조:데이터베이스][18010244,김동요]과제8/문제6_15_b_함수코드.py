class QuadProbing:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size 
        self.d = [None] * size 
        self.N = 0 # 항목 수 

    def hash(self, key):
        return key % self.M
    
    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1 
                return

            if self.a[i] == key:
                self.d[i] = data 
                return
            j += 1 
            i = (initial_position + j*j) % self.M
            if self.N > self.M: # 저장된 항목 수가 테이블 크기보다 크면 [저장실패]
                break 
    def get(self, key): # 탐색연산 
        initial_position = self.hash(key)
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + j*j) % self.M
            j += 1 
        return None 

    def print_table(self): # 해쉬 테이블 출력 
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
                
        print()