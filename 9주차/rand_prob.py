import random

class RandProbing:
    
    def __init__(self, size):
        self.M = size
        self.a = [None] * size 
        self.d = [None] * size 
        self.N = 0 # 항목 수 


    def hash(self, key):
        return key % self.M
    

    def put(self, key, data): # 삽입연산 
        initial_position = self.hash(key)
        i = initial_position
        random.seed(1000)
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1 
                return

            if self.a[i] == key:
                self.d[i] = data 
                return
            j = random.randint(1, 99) # 난수 크기 범위 지정 
            i = (initial_position + j) % self.M
            if self.N > self.M:
                break

    
    def get(self, key): 
        initial_position = self.hash(key)
        i = initial_position
        random.seed(1000)
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + random.randint(1, 99)) % self.M
        return None 

    


    def print_table(self): # 해쉬 테이블 출력 
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
                
        print()

