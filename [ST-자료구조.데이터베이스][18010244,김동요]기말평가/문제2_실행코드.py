# 문제 2 실행 코드 
# 랜덤조사 

from 문제2_함수코드 import RandProbing
if __name__ == '__main__':
    t = RandProbing(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon') 
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

    # 잘 삽입이 되었나 확인 
    print('23, 48 삽입 후 해시 테이블:')
    t.print_table()
    print()
    # 삽입이 원할하게 랜덤조사 방식으로 삽입 되었다는 것을 확인 

    # 다시 탐색
    print('새로운 값  삽입 후 탐색 결과:')
    print('23의 data = ', t.get(23))
    print('48의 data = ', t.get(48))
    print()

    # 찾는 키가 없는 경우
    print('찾는 키가 없는 경우:')
    print('52의 data = ', t.get(52))

    