# 문제 3: 이중해싱를 위한 파이썬 프로그램을 작성하시오. 

'''이중해싱은 2개의 해시 함수(h(key), d(key))를 사용하는 충돌 해결 방법입니다. 두 해쉬 함수 중 하나는 기본적인 해시함수(h(key)로 해시 값을 
해시 테이블의 인덱스로 변환하고 제 2의 함수(d(key))는 충돌이 발생하면, 다음 위치를 위한 점프 크기를 규칙에 따라 정해줍니다.
초기 __inint__은 이전 랜덤 조사와 동일하게 지정해주었으며, 삽입 함수에서는 새롭게 충돌이 발생하면 발동할 d 함수(d = 7 - (key % 7))를 만들어 주었으며,
만약 충돌이 발생하면, j가 0부터 1씩 증가하고 d(key) 함수에서 나온 값을 이용하여 다음 위치를 위한 점프 크기를 정해주었습니다.
또한, 만약 삽입을 할떄, 저장된 항목 수가 해시 테이블의 크기보다 크게되면 삽입을 중지하게끔 조건을 만들어 주었습니다. 
탐색(get())을 진행할 떄도 삽입함수와 유사하게 점프 크기를 정해줄 d 함수를 새롭게 만들어 주었고, 만약 해당 인덱스의 키 값이 일치하지 않으면 
다음 원소 검사를 위해 i 값을 업데이트 해주며 j 값도  1씩 증가시켜 주었습니다. 
다음으로 삭제(delete) 함수를 구현해봤는데, 저는 이전에 삭제된 원소를 None으로 바꿔 주었지만, 나중에 탐색 연산을 했을 때, 해당 해시 값이 None이면 조건에 따라
탐색 자체를 실패하는 문제가 있었습니다. 그래서 삭제할 원소를 None이 아닌 <delete>로 변경해주어 탐색을 원할하게 할 수 있도록 만들어 주었습니다.
또한, 저장된 항목 수에서 1를 빼주었습니다.  
삭제한 원소의 값을 <delete>로 바꾸면, 나중에 새로운 키의 삽입을 진행할 때, None이 아니기 떄문에, 해당 자리에 삽입을 안하는 문제가 
발생했습니다. 그래서 기존의 삽입 함수에 새로운 조건(self.a[i] == None or self.a[i] == '<delete>': 삽입 진행)을 추가해주어서 만약 해당 
리스트의 값이 None이거나 <delete>인 경우 그 자리에 새로운 키를 저장할 수 있도록 만들어 주었습니다. 또한, 삭제할 key의 인덱스만 반환해주는 함수(get_index)를 새로 만들어 주어서,
 삭제할 key의 인덱스를 파악하여 그 위치의 값을 <delete> 로 원할하게 바꾸고 data 값을 None으로 바꿀 수 있었습니다. 
'''



# 이중해싱 
class DoubleHashing: 
    def __init__(self, size):
        self.M = size # 테이블 크기
        self.a = [None] * size # 해시테이블 a 
        self.d = [None] * size # 데이터 저장용 d 
        self.N = 0 # 항목수 

    def hash(self, key):
        return key % self.M # 나눗셈 해시함수


    
    def put(self, key, data): # 삽입연산
        # 해시값을 변수에 저장
        initial_position = self.hash(key) 
        # 초기 위치를 i에 저장(업데이트를 용이하게 해주기 위해) 
        i = initial_position
        # 점프 크기를 정해줄 d 함수를 새롭게 만들어 준다. 
        d = 7 - (key % 7)
        j = 0
        while True:
             #  None인 자리에만 값을 넣어주는 문제를 해결하기 위해, '<delete>'을 발견하면 값을 넣어 주는 조건을 추가  
            if self.a[i] == None or self.a[i] == '<delete>': # 빈곳 발견 
                # 해당 인덱스(해시값)에 값을 넣어준다 
                self.a[i] = key # 키는 해시테이블에 data는 리스트 d에 저장 
                self.d[i] = data 
                # 원소가 새롭게 저장이 되었으므로, N(저장된 항목수)에서 1을 더해준다. 
                self.N += 1 
                return
            # key가 이미 해시테이블에 있으므로 data만 갱신 
            if self.a[i] == key: 
                self.d[i] = data
                return
            j += 1 
            # j는 충돌이 일어날때 마다 1씩 증가한다(0, 1, 2, 3, 4, ...)
            # d 함수의 결과값에 따라 점프의 크기가 정해진다. 
            i = (initial_position + j * d) % self.M
            # 테이블이 full(저장된 항목이 해시 테이블의 크기보다 크면)이면 삽입을 중단한다. 
            if self.N > self.M:
                break 
    
    def delete(self, key):
        # 삭제할 key의 인덱스만 반환해주는 함수를 새로 만들어 주었다. 
        idx = self.get_index(key)
        # 반환 한 index(i)를 이용하여 값들을 제거해줌 
        # 해쉬 테이블의 해시 값(인덱스)를 <delete>로 바꿔주고, data는 None으로 바꿔준다. 
        self.a[idx] = '<delete>'
        self.d[idx] = None
        # 삭제를 한 거니까, 항목수를 한개 줄여준다. 
        self.N -= 1 
    

    def get(self, key): # 탐색연산 
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        # 점프 크기를 정해줄 d 함수를 새롭게 만들어 준다. 
        d = 7 - (key % 7)
        j = 0
        while self.a[i] != None:
            if self.a[i] == key:
                # 만약 해당 자리에 key값이 있다면, 탐색 성공(해당 인덱스의 data 값을 리턴)
                return self.d[i] # 탐색 성공      
            # 다음 원소 검사를 위해 i 값을 업데이트 해준다. 
            i = (initial_position + j * d) % self.M 
            # j는 key가 일치하지 않을 때 마다 1씩 증가한다(0, 1, 2, 3, 4, ...)
            j += 1 
        # 탐색 실패 
        return None 

    def get_index(self, key): # 탐색하려는 키의 인덱스를 반환하는 함수  
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        # 점프 크기를 정해줄 d 함수를 새롭게 만들어 준다.
        d = 7 - (key % 7)
        j = 0
        while self.a[i] != None:
            # 만약 해당 자리에 key 값이 있다면, 해당 리스트의 인덱스를 반환 
            if self.a[i] == key:
                return i  # 탐색 성공(해당 인덱스 반환)
            i = (initial_position + j * d) % self.M #다음 원소 검사를 위해 
            j += 1 
        # 탐색 실패 
        return None 

     # 교과서를 참고해서 코드를 작성 
    def print_table(self): # 해시 테이블 출력 
        # 반복문을 이용해서 해시 테이블의 크기 만큼 반복: 해시 테이블의 인덱스를 보기 쉽게 표현하기 위해 
        for i in range(self.M):
            print('{:4}'.format(str(i)), ' ', end='')
        print()
        # 실제 해시 테이블에 저장되어 있는 key들을 반복문을 통해 이어서 출력 
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), ' ', end='')
                
        print()