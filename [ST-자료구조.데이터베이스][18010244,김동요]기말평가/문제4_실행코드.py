# 문제 4 실행코드
# 2-방향 체이닝 

from 문제4_함수코드 import TwoWayChaining
if __name__ == '__main__':
    t = TwoWayChaining(13)
    t.put(25, 'grape')
    t.put(37, 'apple')
    t.put(18, 'banana')
    t.put(55, 'cherry')
    t.put(22, 'mango')
    t.put(35, 'lime')
    t.put(50, 'orange')
    t.put(63, 'watermelon')
    print('해시 테이블 : ')
    t.print_table()
    print()
    '''25, 37, 18, 55, 22 까지는 충돌없이 저장이 되는데, 다음으로 35의 기본 해시값은 9인데, a[9]에는 이미 22가 있다는 것을 확인
    2-방향 체이닝은 2개의 해시함수를 이용하여 연결리스트의 길이가 짧은 쪽에 새 키를 저장하기 떄문에, a[9]은 이미 22이 있으니
    길이(length)가 1이고 다른 해시함수 d = ((35%11) * 23)%13 = 7이고 a[7]의 길이는 0이므로 길이가 더 짧은 a[7]에 35를 저장한다.
    다음으로 50을 저장해야 되는데, 50의 기본 해시값은 11이고 a[11]에는 이미 37이 있다는 것을 확인(충돌) a[11]의 길이(length)는 1이고 
    다른 해시함수 d = ((50%11) * 23)%13 = 8이고 a[8]의 길이는 0이므로 길이가 더 짧은 a[8]에 50을 저장한다.
    마지막으로 63을 저장해야 되는데, 63의 기본 해시값은 11이고 a[11]에는 이미 37이 있다는 것을 확인(충돌) a[11]의 길이(length)는 1이고
    다른 해시함수 d = ((63%11) * 23)%13 = 2이고 a[2]의 길이는 0이므로 길이가 더 짧은 a[2]에 63을 저장한다. '''

    # 삽입 
    # 추가적으로 몇 개의 값들을 더 저장하여 연결 리스트의 길이를 좀 더 늘려주었다(삭제 메소드가 잘 적용되는 확인하기 위해 연결 리스트의 길이를 늘려준다).
    t.put(51, 'kiwi')
    t.put(24, 'pineapple')
    t.put(46, 'lemon')
    print('51, 23, 48 삽입 후 해시 테이블 :')
    t.print_table()
    print()
    
    # 탐색 
    print('탐색 결과:')
    print('50의 data = ', t.get(50))
    print('63의 data = ', t.get(63))
    print('22의 data = ', t.get(22))
    print()



    t.delete(18)
    t.delete(37)
    t.delete(51)
    print('18, 37, 51 삭제 후 해시테이블 : ')
    t.print_table()
    print()

        
    # 탐색 
    print('삭제 후 탐색 결과:')
    print('50의 data = ', t.get(50))
    print('63의 data = ', t.get(63))
    print('18의 data = ', t.get(18))
