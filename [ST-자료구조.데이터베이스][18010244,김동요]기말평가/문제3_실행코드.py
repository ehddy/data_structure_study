# 문제 3 실행 코드
# 이중 해시 

from 문제3_함수코드 import DoubleHashing
if __name__ == '__main__':
    t = DoubleHashing(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon') 
    '''25, 37, 18, 55, 22는 충돌 없이 각각 해시값에 해당되는 1차원 리스트 원소에 저장됩니다. 
    하지만, 35를 저장하는 경우 h(35) = 9이므로 a[9]에 저장해야 되지만, 이미 a[9]에 22가 있어 충돌이 발생합니다. 
    따라서, j =1 일때는 (h(35) + 1 X d(35)) % 13 = 3으로 a[3]에 저장해야 되지만, 이미 55가 있어 또 다시 충돌이 발생합니다. 
    이번에는 j가 2가 되고 (h(35) + 2 X d(35)) % 13  = 10이 되어 a[10]에는 값이 비어있으므로 35를 넣어줍니다. 
    '''
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
    print('35의 data = ', t.get(35))
    print('63의 data = ', t.get(63))
    print()

    # 새로운 값을 삽입 
    t.put(23, 'pineapple')
    t.put(48, 'lemon')
    '''23의 해쉬 값은 10(h(23) = 10)이므로, a[10]에 저장 되어야 하지만, 이미 그 자리에 35가 있다. 
    따라서 j = 1일떄, (h(23) + 1 X d(23)) % 13 = 2이므로 a[2]에는 비어있기 때문에. a[2]에 23을 삽입해주는 것을 확인
    48의 해쉬 값은 9이므로 a[9]에 값이 비어있으므로 a[9]에 48을 삽입한다.'''

    # 잘 삽입이 되었나 확인 
    print('23, 48 삽입 후 해시 테이블:')
    t.print_table()
    print()
    # 삽입이 원할하게 이중해싱 방식으로 삽입 되었다는 것을 확인 
    
    # 다시 탐색
    print('새로운 값  삽입 후 탐색 결과:')
    print('23의 data = ', t.get(23))
    print('48의 data = ', t.get(48))
    print()

    # 찾는 키가 없는 경우
    print('찾는 키가 없는 경우:')
    print('52의 data = ', t.get(52))