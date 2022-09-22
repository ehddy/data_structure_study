from binary_heap_4_32 import BHeap_max
if __name__ == '__main__':
    a = [None] * 1
    b = BHeap_max(a)
    print('최대힙 삽입 전: empty')
    b.print_heap()
    print()


    # 빈 최대힙에 순차적으로 삽입 
    b.insert(10)
    b.insert(50)
    b.insert(20)
    b.insert(60)
    b.insert(30)
    b.insert(70)
    b.insert(40)
    b.insert(80)
    print('순차적으로 삽입 후 최대 힙: ')
    b.print_heap()
    print()

    # 추가적으로 삭제 함수를 만들었습니다. 
    print('삭제전 최대값', b.delete_max())
    print('최대값 삭제 후:')
    b.print_heap()
    
