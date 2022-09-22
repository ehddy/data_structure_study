# 문제 5 실행코드 
# 뻐꾸기 해싱 

from 문제5_함수코드 import CuckooHashing
if __name__ == '__main__':
    t = CuckooHashing(13)
    t.put(14)
    t.put(15)
    t.put(27)
    t.put(60)
    t.put(52)
    t.put(37)
    t.put(22)
    t.put(30)
    t.put(13)
    t.put(26)
    t.put(17)
    ''' 14, 15는 충돌없이 삽입이 되다가, 27과 14가 충돌하여, 14가 d[4]로 쫒겨난다. 다음으로, 60, 52, 37, 22, 30이 층돌 없이 
    h[]에 저장이 되다가 13이 52를 쫒아내고 h[0]으로 52는 d[2]에 저장 된다. 또한 26을 저장할 떄, 13이랑 충돌이 발생하고, 13은 쫒겨나서
    d[7]에 저장된다. 마지막으로, 17을 저장할 때, 30과 충돌하고 30이 d[2]으로 이동하면서, 또 d[2]에 이미 있는 52와 충돌이 발생한다. 
    52는 쫒겨나서, a[0]에 저장되고 또한, a[0]에 이미 저장되어 있던, 26은 다시 쫒겨나서 d[1]에 저장된다.'''

    print('뻐꾸기 해싱 결과 테이블: ')
    t.print_table()
    print()

    print('52, 14 탐색')
    t.get(52)
    t.get(14)
    print()

    print('17, 13 삭제 후 결과 테이블 :')
    t.delete(17)
    t.delete(13)
    t.print_table() 
    print()


    print('삭제 후 탐색:')
    t.get(14)
    t.get(22)
    print()