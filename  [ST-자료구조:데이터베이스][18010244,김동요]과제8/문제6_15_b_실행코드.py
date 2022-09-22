from 문제6_15_b_함수코드 import QuadProbing
if __name__ == '__main__':
    t = QuadProbing(11)
    t.put(71, '')
    t.put(23, '')
    t.put(73, '')
    t.put(49, '')
    t.put(54, '')
    t.put(89, '')
    t.put(39, '')

    print('탐색 결과:')
    print('해쉬테이블:')
    t.print_table()