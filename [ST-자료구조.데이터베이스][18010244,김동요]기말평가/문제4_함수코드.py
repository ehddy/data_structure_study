# 문제 4: 2-방향 체이닝을 파이썬 프로그램으로 구현하시오

'''2-방향 체이닝은 일반 체이닝과 비슷히지만, 2개의 해시함수를 이용하여 연결리스트의 길이가 짧은 쪽에 새 키를 저장합니다.
책에 구현되어 있는 체이닝 코드를 참고했으며, 새롭게 해당 a[index] 내에 있는 연결리스트의 길이 변수(length)를 추가해주었습니다. 
length를 통해 각 두개의 함수를 비교해 길이가 짧은 쪽의 연결리스트에 key를 삽입해주었습니다. 탐색(get)도 이와 비슷한 방법으로
해당 key는 2 가지 경우의 수로 저장될 수 밖에 없으니 2개의 함수에서 모두 탐색을 진행하여 탐색을 진행했습니다. key의 제거(delete)를 코드로 
구현하는데 많은 어려움이 있었으며, prev와 p를 이동시키면서 연결리스트 안에서 탐색을 진행했고, 노드가 맨 앞에 있는 경우, 뒤에 있는 경우, 그 외의 경우
를 모두 고려하여 코드를 작성해보았습니다. 구체적인 내용은 해당 코드에 주석에다 상세하게 달아놓았습니다.'''


class TwoWayChaining:
    # 노드 객체를 생성 
    class Node:
        def __init__(self, key, data, link):
            self.key = key # 해당 노드의 키 
            self.data = data  # 해당 노드의 값
            self.next = link  # 해당 노드의 다음 값(오른쪽 값)

    # TwoWayChaining의 객체를 생성 
    def __init__(self, size):
        self.M = size # 해시 테이블의 크기 
        self.a = [None] * size # 해시 테이블 a
    

    def hash(self, key):
        return key % self.M # 나눗셈 해시함수
    

    def put(self, key, data): # 삽입 연산 
        # 삽입해줄 key의 해시값을 i 변수에 저장 
        i = self.hash(key)
        # 해쉬 테이블의 i 값을 p에 저장 
        p = self.a[i]
        # 일단 해당 연결리스트의 길이를 0으로 설정 
        length = 0     
        # 길이가 얼마나 되는지 파악하기 위해 반복문 실행 
        while p != None:
            # 만약 이미 키 값이 있다면, data만 갱신해주고 return한다 
            if key == p.key:
                p.data = data
                return
            # 반복적으로 연결리스트를 next 방향으로 이동(p가 None이 될 때까지)
            p = p.next
            # p가 있다는 것이므로, 길이를 1 증가, 반복문이 끝나면 길이 값이 갱신되어 있을 것이다. 
            length += 1 
        
        # 충돌이 발생했을 경우 비교할 다른 해시 함수 설정 
        # d 다른 해시 함수의 해시값을 d에 저장 
        d = ((key%11) * 23)%13
        # 해쉬 테이블의 d(index) 값을 d_value에 저장 
        d_value = self.a[d]
        # 일단 해당 연결리스트의 길이(d_length)를 0으로 설정 
        d_length = 0
        # 길이가 얼마나 되는지 파악하기 위해 반복문 실행 
        while d_value != None: 
            # 삽입은 마지막에 진행해주고 일단 길이만 파악
            d_value = d_value.next
            # d_value가 있다는 것이므로, 길이를 1 증가, 반복문이 끝나면 길이 값이 갱신되어 있을 것이다. 
            d_length += 1 
        
        # 최종적으로 기본 해시 함수의 해당 인덱스의 연결리스트의 길이와, 다른 해시함수의 해당 인덱스의 연결리스트의 길이를 비교 
        # 기본 해시 함수의 길이가 0이라는 것은 아무 값이 저장되어 있지 않다는 것이므로, 기본 해시 값의 인덱스에 값을 저장 
        # 기본 해시 함수와 다른 해시 함수(d)을 이용하여 연결리스트의 길이가 짧은 쪽에 새로운 키를 저장한다.
        if length == 0 or length <= d_length:
            self.a[i] = self.Node(key, data, self.a[i])
        # 만약 길이가 다른 함수(d)가 더 짧다면 
        else:
            self.a[d] = self.Node(key, data, self.a[d])

    

    # 탐색은 만약 삽입을 하면, 삽입되는 해시 테이블의 인덱스가 2개(기본해시 함수의 인덱스, 다른 해시 함수의 인덱스)로 좁혀지므로 
    # 2가지 경우를 모두 다 코드로 작성해보았다.  
    def get(self, key): # 탐색 연산 

        # i 해시함수를 이용한 연결리스트의 해당 값이 있는 경우
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:
                return p.data
            p = p.next 
        
        # d 해시함수를 이용한 연결리스트의 해당 값이 있는 경우
        d = ((key%11) * 23)%13
        d_value = self.a[d]
        while d_value != None:
            if key == d_value.key:
                return d_value.data
            d_value = d_value.next 
        
        # 만약 둘 다 없는 경우 탐색 실패 
        return None

    # 삭제할 key의 인덱스를 파악하기 위해 새로운 함수를 구현해보았다(return i(인덱스)를 제외하고 get()함수와 동일)
    def get_index(self, key): # 탐색 연산 
        # i 해시함수를 이용한 연결리스트의 해당 값이 있는 경우
        i = self.hash(key)
        p = self.a[i]
        while p != None:
            if key == p.key:
                return i
            p = p.next 
        
        # d 해시함수를 이용한 연결리스트의 해당 값이 있는 경우
        d = ((key%11) * 23)%13
        d_value = self.a[d]
        while d_value != None:
            if key == d_value.key:
                return d
            d_value = d_value.next 
        # 탐색 실패 
        return None


    def delete(self, key):
        # 삭제할 key의 인덱스만 반환해주는 함수를 새로 만들어주었다.
        # 삭제할 key의 인덱스를 변수에 저장 
        idx = self.get_index(key)
        # 삭제할 노드의 연결리스트 = p 
        p = self.a[idx]

        # 이전 노드의 초기 값을 None으로 설정 
        prev = None
        while p != None:
            # 연결리스트의 해당 key가 일치할 때 까지 반복 
            if key == p.key:
                # 만약 이전 값이 있다면, 이전 값의 next는 p가 아니라, p의 next가 되어야 연결되기 때문에, 현재 p는 자연스럽게 삭제가 된다. 
                if prev != None: 
                    prev.next = p.next
                # 만약 이전(prev) 값이 없다면(else), 현재 p(삭제할 값)가 맨 앞의 노드라는 것 이므로, self.a[idx]와  p의 next로 연결해준다. 
                # 그 다음 값(p.next)과 연결 되어, 자연스럽게 p는 삭제가 된다. 
                else:
                    self.a[idx] = p.next 
                
                # 해당 값의 삭제를 진행하고 최종적으로 return 
                return 

            # 만약 key가 일치하지 않으면 p의 다음 값(next)으로 옮기고 
            # next를 p로, 기존의 p를 prev(이전값)에 저장해준다.
            prev = p 
            p = p.next 
        

    # 교과서를 참고해서 코드를 작성 
    def print_table(self): # 테이블 출력 
        for i in range(self.M):
            print('%2d' % (i), end='')
            p = self.a[i]
            # 연결리스트에 있는 모든 key 값들을 나열 
            while p != None:
                print('-->[', p.key, ',', p.data, ']', end='')
                # p가 None이 될때까지 이동 
                p = p.next
            print()



