from binary_heap_4_19 import BHeap
if __name__ == '__main__':
    a = [None] * 1
    a.append(10)
    a.append(20)
    a.append(25)
    a.append(30)
    a.append(40)
    a.append(50)
    a.append(45)
    b = BHeap(a)
    b.create_heap()
    print('최소힙:')
    b.print_heap()
    max_value = b.max_value_downheap(1) # 최대값을 찾는 메소드 
    print('최소힙 최대값 : {}'.format(max_value)) 


