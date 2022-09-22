class BHeap:
    def __init__(self, a):
        self.a = a
        self.N = len(a) -1 

    def create_heap(self): # 초기 힙 만들기
        for i in range(self.N//2, 0, -1):
            self.downheap(i)
   
    def insert(self, key_value): # 삽입연산 
        self.N += 1 
        self.a.append(key_value)
        self.upheap(self.N)

    def delete_min(self): # 최소값 삭제 
        if self.N == 0:
            print('합이 비어 있음')
            return None
        minimum = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -= 1 
        self.downheap(1)
        return minimum
    
    def downheap(self, i): # 힙 내려가며 힙속성 회복 
        while 2*i <= self.N:
            k = 2 * i
            if k < self.N and self.a[k] > self.a[k+1]:
                k += 1
            if self.a[i] < self.a[k]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k 

  # 최소힙에서 최댓값을 찾는 이 함수는 루트노드로부터 이파리 방향으로 각 노드에서 큰 자식으로 내려가면 최댓값을 가진 노드에 도달
  # Downheap() 방식으로 큰 값을 찾아나가면서 i를 바꿔주는데, 이는 높이에 비례하므로 수행시간은 log(n+1) => o(log(N))이다. 
    def max_value_downheap(self, i): # 최소힙 내려가며 최대값을 찾는 함수  
        while 2*i <= self.N:
            k = 2 * i
            if k < self.N and self.a[k] < self.a[k+1]:
                k += 1 
            if self.a[i] > self.a[k]:
                break
            i = k 
        return self.a[i]
            

    def upheap(self, j): # 힙을 올라가며 힙속성 회복 
        while j > 1 and self.a[j//2] > self.a[j]:
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j = j//2 
    

    def print_heap(self): # 힙 출력 
        for i in range(1 ,self.N+1):
            print("[{}]".format(self.a[i]))
        print('\n힙크기 = ', self.N)
 
