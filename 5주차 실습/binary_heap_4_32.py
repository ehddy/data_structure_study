# 최대힙 만들기 
class BHeap_max:
    def __init__(self, a):
        self.a = a
        self.N = len(a) -1 

    def create_heap(self): # 초기 힙 만들기
        for i in range(self.N//2, 0, -1):
            self.downheap(i)
   
    def insert(self, key_value): # 삽입연산 # 맨 끝 값에 넣어준다음 부모 노드와 값을 비교해서 만약 부모 노드보다 값이 크다면 위치를 바꾼다. 
        self.N += 1 
        self.a.append(key_value)
        self.upheap(self.N)

    def delete_max(self): # 최대값 삭제 
        if self.N == 0:
            print('합이 비어 있음')
            return None
        max = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.N -= 1 
        self.downheap(1)
        return max
    
    def downheap(self, i): # 힙 내려가며 힙속성 회복 
        while 2*i <= self.N:
            k = 2 * i
            if k < self.N and self.a[k] < self.a[k+1]:
                k += 1
            if self.a[i] > self.a[k]:
                break
            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k 

    def upheap(self, j): # 힙을 올라가며 힙속성 회복, 
        while j > 1 and self.a[j//2] < self.a[j]:
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j = j//2 
    
    def print_heap(self): # 힙 출력 
        for i in range(1 ,self.N+1):
            print("[{}]".format(self.a[i]))
        print('\n힙크기 = ', self.N)
 