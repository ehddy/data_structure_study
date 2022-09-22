# 문제 1 실행 코드 
# 선형조사 

from 문제1_함수코드 import LinearProbing
if __name__ == '__main__':
    t = LinearProbing(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon') 
    '''25, 37, 18, 55, 22는 충돌 없이 각각 해시값에 해당되는 리스트 원소에 저장이 된다. 하지만, 35를 저장하려는 경우
    h(35) = 9이므로 a[9]에 저장해야 하지만 a[9]에는 이미 22가 있어 충돌이 발생한다. 이떄 선형 조사 방식으로 a[9+1] = a[10]을 
    검사하고 10이 비어있으므로 a[10]에다 35를 넣어준다. 50과 63을 삽입할 때도 각각 충돌이 발생하며 선형 조사 방식으로 빈 원소를 찾아
    저장이 된다.'''
    print('탐색 결과:')
    print('50의 data = ', t.get(50))
    print('63의 data = ', t.get(63))
    print()

    print('해시테이블:')
    t.print_table()
    print()

    # 원소 22를 삭제 
    t.delete(22)

    # 삭제한 후 다시 테이블 출력 
    print('22 삭제후 해시 테이블:')
    t.print_table()
    print()

    # 탐색이 잘 되었나 확인 
    print('22 삭제 후 탐색:')

    '''만약 22의 해시 값인 9에 자리를 None으로 바꿔주었으면, 원래 해시 값이 9였지만, 10으로 밀려난 원소 35의 탐색이 안되었을텐데, 
    다른 값으로 바꿔주어 원할하게 탐색이 되었다는 것을 확인'''
    print('35의 data = ', t.get(35))
    print('63의 data = ', t.get(63))
    print()

    # 새로운 값을 삽입 
    t.put(23, 'pineapple')
    t.put(48, 'lemon')
    '''23의 해시 값은 10이므로 a[10]에 저장을 해야 되는데, a[10에는] 이미 35가 들어가있어, 선형 조사 방식으로 반복적으로 a[10+j] 만큼 이동하여  
    (j = 0, 1, 2, 3 ...) 결국 a[2]가 비어있어 a[2]에 23을 저장한다. 48은 충돌하지 않고 바로 a[9]에 삽입했다. 
    '''

    # 잘 삽입이 되었나 확인 
    print('23, 48 삽입 후 해쉬 테이블:')
    t.print_table()
    print()
    # 삽입이 원할하게 선형조사 방식으로 삽입 되었다는 것을 확인 

    # 다시 탐색
    print('새로운 값  삽입 후 탐색 결과:')
    print('23의 data = ', t.get(23))
    print('48의 data = ', t.get(48))
    print()

    # 찾는 키가 없는 경우
    print('찾는 키가 없는 경우:')
    print('52의 data = ', t.get(52))