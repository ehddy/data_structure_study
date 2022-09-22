# 문제 5: 뻐꾸기해싱을 파이썬 프로그램으로 구현하시오

'''뻐꾸기 해싱은 2개의 해시함수와 각 함수에 대응되는 해시테이블을 이용해 충돌이 발생하면 그 곳에 있는 키를 쫒아내는 해싱 기법입니다.
먼저 두개의 테이블을 만들어 주었습니다(self.h, self.d)
삽입과정은 key에 저장할 원소가 비어있으면, 삽입을 진행해주고, 만약 삽입할 자리에 다른 key가 있으면, 그 key를 다른 해시 함수를 이용해 
해시 값을 구해준다음, 그 해시 함수에 대응되는 해시 테이블에 넣어주었습니다. 또, 그 해시 테이블에도 다른 key가 있다면, 그 기존의 키를 또다시 쫒아내고
쫒아낸 그 키를 다시 원래 해시 함수를 이용해서 값을 구해준다음, 그 기존 해시 함수에 대응되는 해시 테이블에 넣어주었습니다.
코드를 구현하는 데 가장 오랜 시간이 걸린 함수는 삽입 함수이며, 처음에는 재귀호출을 해보려 했지만, 실패하였고, 반복문을 이용해서 풀어보았습니다.
탐색함수와 제거함수는 2가지 경우의 수를 고려하여 비교적 쉽게 구현했습니다.  
각각 함수에 대한 구체적인 설명은 함수 주석에 달아놓았습니다. 
 '''

# 뻐꾸기 해싱 
class CuckooHashing:

    def __init__(self, size):
        self.M = size 

        # htable
        self.h = [None] * size

        # dtable
        self.d = [None] * size

    
    # 나눗셈 해시함수(h(key))
    def hash(self, key):
        return key % self.M 

    # 또 다른 해시함수(d(key))
    def d_key(self, key):
        return ((key%11) * 23)%13

    # 삽입 함수
    ''''만약 해당 자리에 이미 값이 있다면  new_key(index)와 key를 반복문을 통해 업데이트 해주는 방식으로 코드를 구현해봤습니다. 
    총 쫒겨나는 경우의 수는 2가지로 설정(key를 넣을 h_tabel(h)에 이미 다른 key가 있는 경우, key를 넣을 d_tabel에 이미 다른 key가 있는 경우)
    이렇게 2가지 경우를 설정했고, 만약 이동했을 경우 또 그 자리에 이미 값이 있을 경우를 고려하여, 만약 그런 상황이 발생한다면, 
    new_key와 key를 반복문을 통해 업데이트 시켜주었으며 업데이트 된 값들은 또 다시 조건문을 통해, 자리를 찾아 삽입이 원할하게 진행되었습니다.'''  
    def put(self, key): 
        # 삽입하길 원하는 key의 해시 값을 new_key에 저장 
        new_key = self.hash(key)
        while True:
            # 만약 key가 저장된 원소가 비어있으면 
            if self.h[new_key] == None: 
                # 키를 해쉬테이블에 저장하고 함수 종료  
                self.h[new_key] = key 
                return

            # 만약 key을 넣을 htabel[new_key]에 이미 다른 key가 있을 경우
            elif self.h[new_key] != None:
                # 쫒아낼 key를  old_key변수에 저장 
                old_key = self.h[new_key]
                # 먼저 쫒아내주고 그 자리에 새로운 키를 삽입 
                self.h[new_key] = key
                # 쫒겨난 key를 d_tabel 해시 함수를 이용하여 해시값을 j에 저장 
                j = self.d_key(old_key)
                # 만약 d_tabel에 자리가 비어있으면 
                if self.d[j] == None:
                    # d[j]에 쫒겨난 키를 삽입하고 함수 종료   
                    self.d[j] = old_key
                    return
                # 만약 d_table에도 자리가 없다면, new_key와 key를 업데이트 시켜주고 반복문 진행 
                # new_key는 해당 d[j]의 key를 다시 기존 h_tabel 해시 함수를 이용하여 해시 값을 구하여 업데이트 
                new_key = self.hash(self.d[j])
                # key는 쫒겨날 d[j]로 업데이트 시켜준다 .
                key = self.d[j]
                # 일단 d[j]에 쫒겨난 old_key를 저장하고 반복문 진행(또 다시 쫒겨난 값을 다른 테이블에 저장시키기 위해) 
                self.d[j] = old_key
             
            
            # 만약 key을 넣을 dtabel[new_key]에 이미 다른 key가 있을 경우
            elif self.d[new_key] != None:
                # 쫒아낼 key를  old_key변수에 저장 
                old_key = self.d[new_key]
                # 먼저 쫒아내주고 그 자리에 새로운 키를 삽입 
                self.d[new_key] = key
                # 쫒겨난 key를 h_tabel 해시 함수를 이용하여 해시값을 j에 저장 
                j = self.hash(old_key)
                # 만약 h_tabel에 자리가 비어있으면 
                if self.h[j] == None:
                     # h[j]에 쫒겨난 키를 삽입하고 함수 종료  
                    self.h[j] = old_key
                    return
                # 만약 h_table에도 자리가 없다면, new_key와 key를 업데이트 시켜주고 반복문 진행 
                # new_key는 해당 h[j]의 key를 다시 기존 d_tabel 해시 함수를 이용하여 해시 값을 구하여 업데이트
                new_key = self.d_key(self.h[j])
                # key는 쫒겨날 h[j]로 업데이트 시켜준다 .
                key = self.d[j]
                # 일단 h[j]에 쫒겨난 old_key를 저장하고 반복문 진행(또 다시 쫒겨난 값을 다른 테이블에 저장시키기 위해) 
                self.h[j] = old_key


    # 탐색 함수
    '''탐색함수는 비교적 삽입함수보다 쉽게 구현해보았는데, 하나의 키가 저장될 수 있는 경우가 2가지(h_table에 저장될 경우, 
    d_tabel에 저장 될 경우)밖에 안되기 때문에, 두 개의 해시함수를 이용한 2개의 해시값을 구해 각각 테이블의 그 key가 있는지 확인하여
    만약 발견한다면, 해당 테이블과 해당 인덱스의 탐색하려는 key가 있다는 것을 보기 쉽게 출력하고 함수를 종료하게 만들었습니다'''
    def get(self, key): 
        # h(key) 해시 함수를 이용해 해시값 저장 
        h_value = self.hash(key)
        # d(key) 해시 함수를 이용해 해시값 저장 
        d_value = self.d_key(key)

        # 먼저 h_table(h) 부터 탐색을 진행
        while self.h[h_value] != None:
            # 만약 해당 해시 값 위치에 key가 있다면 탐색 완료 후 함수 종료 
            if self.h[h_value] == key:
                print('htabel에서 탐색완료 : key = {}은 h[{}]에서 발견'.format(key, h_value))
                return 
            # 만약 없다면 반복문 탈출 
            else:       
                break
        # 다음으로 d_tabel(d)에서 탐색을 진행 
        while self.d[d_value] != None:
            # 만약 해당 해시 값 위치에 key가 있다면 탐색 완료 후 함수 종료 
            if self.d[d_value] == key:
                print('dtabel에서 탐색완료 : key = {}은 d[{}]에서 발견'.format(key, d_value))
                return  
            # 만약 d_tabel에도 없다면 반복문을 탈출하고 None을 리턴하여 함수 종료 
            else:
                break
         # 탐색 실패            
        return None 

    # 삭제 함수
    '''삭제 함수도 탐색 함수와 유사하게 코드를 구현해봤습니다. 하나의 키가 저장될 수 있는 경우가 2가지(h_table에 저장될 경우, 
    d_tabel에 저장 될 경우)밖에 안되기 때문에, 두 개의 해시함수를 이용한 2개의 해시값을 구해 각각 테이블의 그 key가 있는지 확인하여
    만약 발견한다면, 해당 테이블 해당 인덱스의 값을 None으로 변경해주었습니다.'''
    def delete(self, key):
        # h(key) 해시 함수를 이용해 해시값 저장 
        h_value = self.hash(key)
        # d(key) 해시 함수를 이용해 해시값 저장 
        d_value = self.d_key(key)

        # 먼저 h_table(h) 부터 탐색을 진행
        while self.h[h_value] != None:
            # 만약 해당 해시 값 위치에 key가 있다면 해당 테이블의 해당 인덱스의 값을 None으로 변경한 후 함수 종료 
            if self.h[h_value] == key:
                self.h[h_value] = None
                return 
            # 만약 key를 못찾았으면, 다음 탐색을 위해 현재 반복문 탈출 
            else:       
                break
        # 다음으로 d_tabel(d)에서 탐색을 진행       
        while self.d[d_value] != None:
            # 만약 해당 해시 값 위치에 key가 있다면 해당 테이블의 해당 인덱스의 값을 None으로 변경한 후 함수 종료 
            if self.d[d_value] == key:
                self.d[d_value] = None
                return  
            # 만약 d_tabel에도 없다면 반복문을 탈출하고 None을 리턴하여 함수 종료 
            else:
                break
         # 삭제 실패            
        return None 

    # 테이블 출력 함수 
    '''두개의 테이블 h_tabel(h), d_table(d)을 보기 쉽게 표현해보았습니다.'''
    def print_table(self): 
        print('==========================================')
        print('   htable   :   dtable')
        for i in range(self.M):
            print(' {}  [{}]   : {}  [{}]'.format(i, self.h[i], i, self.d[i]))
        print('==========================================')
                

  
    
        


