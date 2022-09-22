# 문제 2 : 랜덤조사를 위한 [프로그램 6-5] rand_prob.py를 작성해라.

'''랜덤조사는 선형조사와 이차조사의 규칙적인 점프 시퀀스와 달리 점프 시퀀스를 무직위화(radient(1, 99)하여 빈 원소를 찾는 충돌 해결 방법입니다.
랜덤 조사는 난수 생성기(random.seed(1000)를 사용하여 다음 위치를 찾는 방법입니다. 
먼저 삽입은 난수 생성 초기값을 설정해주었고, 만약 충돌이 발생한 다면 1, 99까지의 난수로 i를 업데이트 시켜 만약 해당 값이 비어있다면 넣어주는 
랜덤 조사 방식의 삽입을 진행했습니다. 또한, 탐색도 삽입과 동일한 난수 생성 초기값을 설정해주었고, 같은 난수 점프 시퀀스로 탐색을 진행하였습니다. 
특히, 점프 시퀀스로 인해 다시 해시값(initial_position)으로 돌아올 수 있으므로, 선형조사에서 처럼 초기 해쉬값으로 돌아오면 삽입이나 탐색을 
중지하는 조건을 삭제해주었으며, __init__에 저장된 항목수를 나타내는 self.N = 0을 넣어주어 만약 삽입을 할떄, 저장된 항목수가 해시 테이블의 크기
보다 크게되면 삽입을 중지하게끔 조건을 만들어 주었습니다. 
다음으로 삭제(delete) 함수를 구현해봤습니다. 
저는 삭제된 원소를 처음에 None으로 바꿔 주었지만, 나중에 탐색 연산을 했을 때, 해당 해시 값이 None이면 조건에 따라
탐색 자체를 실패하는 문제가 있었습니다. 그래서 삭제할 원소를 None이 아닌 <delete>로 변경해주어 탐색을 원할하게 할 수 있도록 만들어 주었습니다.
또한, 저장된 항목 수에서 1를 빼주었습니다.  
삭제한 원소의 값을 <delete>로 바꾸면, 나중에 새로운 키의 삽입을 진행할 때, None이 아니기 떄문에, 해당 자리에 삽입을 안하는 문제가 
발생했습니다. 그래서 기존의 삽입 함수에 새로운 조건(self.a[i] == None or self.a[i] == '<delete>': 삽입 진행)을 추가해주어서 만약 해당 
리스트의 값이 None이거나 <delete>인 경우 그 자리에 새로운 키를 저장할 수 있도록 만들어 주었습니다. 또한, 삭제할 key의 인덱스만 반환해주는 함수(get_index)를 새로 만들어 주어서, 
삭제를 원할하게 진행했습니다. 
대부분의 코드는 책에 나와있는 이차조사 코드를 참고하여 작성했습니다.(세부적인 내용은 주석에) '''

import random

class RandProbing:
    
    def __init__(self, size):
        # 테이블의 크기 M
        self.M = size
        # 해시 테이블 a 
        self.a = [None] * size 
        # 데이터 저장용 d
        self.d = [None] * size 
        # 저장된 항목 수
        self.N = 0 # 항목 수 

    # 나눗셈 해시 함수 
    def hash(self, key):
        return key % self.M
    

    def put(self, key, data): # 삽입연산 
        # 해시 값을 저장 
        initial_position = self.hash(key)
        # 초기 위치 
        i = initial_position
        # 난수 생성 초기값 
        random.seed(1000)
        while True:
            #  None인 자리에만 값을 넣어주는 문제를 해결하기 위해, '<delete>'을 발견하면 값을 넣어 주는 조건을 추가  
            if self.a[i] == None or self.a[i] == '<delete>':
                # 해당 인덱스(해시값)에 값을 넣어준다 
                self.a[i] = key
                self.d[i] = data
                self.N += 1 # 값을 저장했으므로 저장된 항목수(N)에 1을 더해준다. 
                return

            if self.a[i] == key:
                self.d[i] = data # key가 이미 해시테이블에 있으므로 data만 갱신 
                return
            # 랜덤 조사이기 때문에, 난수의 크기 범위를 지정해준다. 
            j = random.randint(1, 99) # 난수 크기 범위 지정 
            # 다음 원소 검사를 위해  i를 업데이트 
            i = (initial_position + j) % self.M
            # 만약 N이 M 보다 크다는 것은 저장된 항목 수가 테이블 크기보다 크다는 것으로 저장을 더이상 하면 안된다. 
            if self.N > self.M:
                break

         
    def delete(self, key):
         # 삭제할 key의 인덱스만 반환해주는 함수를 새로 만들어 주었다. 
        idx = self.get_index(key)
        # 반환 한 index(i)를 이용하여 값들을 제거해줌 
        # 해시 테이블의 해시 값(인덱스)를 <delete>로 바꿔주고, data는 None으로 바꿔준다. 
        self.a[idx] = '<delete>'
        self.d[idx] = None
        # 항목수를 한개 줄여준다. 
        self.N -= 1 


    def get(self, key): 
        # 해시값을 변수에 저장(다음 원소 검사를 위해)
        initial_position = self.hash(key)
        i = initial_position
        # 저장할 때와 동일한 난수 생성 초기 값 
        random.seed(1000)
        while self.a[i] != None:
            if self.a[i] == key:
                # 만약 해당 자리에 key값이 있다면, 탐색 성공(해당 인덱스의 data 값을 리턴)
                return self.d[i]
            # 다음 원소 검사를 위해 i 값을 업데이트 해준다. 
            i = (initial_position + random.randint(1, 99)) % self.M
        # 탐색 실패 
        return None 

    # 삭제할 key의 인덱스만 반환해주는 함수를 새로 만들어 주었다.
    def get_index(self, key): 
        initial_position = self.hash(key)
        i = initial_position
        random.seed(1000)
        while self.a[i] != None:
            if self.a[i] == key:
                # 만약 해당 자리에 key 값이 있다면, 해당 리스트의 인덱스를 반환 
                return i
             # 다음 원소 검사를 위해 i 값을 업데이트 해준다. 
            i = (initial_position + random.randint(1, 99)) % self.M
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

