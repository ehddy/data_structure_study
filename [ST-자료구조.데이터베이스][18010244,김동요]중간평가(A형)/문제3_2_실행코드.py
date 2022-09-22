from 문제3_2_함수코드 import BST
if __name__ == '__main__':
    t = BST()
    # 노드 삽입 
    t.put(5, 'A')
    t.put(4, 'B')
    t.put(7, 'C')
    t.put(6, 'D')
    t.put(3, 'E')
    t.put(9, 'F')
    t.put(8, 'G')
    def kth_small(k): # 깔끔하게 출력하기 위해 새로운 함수를 만들어 주고 그 안에서 kth_smallest 메서드를 실행 
        # k번째로 작은 key값 
        key = t.kth_smallest(k)[0]
        # k번째로 작은 value값 
        value = t.kth_smallest(k)[1]
        print('{}번째로 작은 값의 key = {}, value = {}'.format(k, key, value))
    
    # 함수 실행 # 0번째 작은 값부터 ~ k번째 작은 값까지 
    kth_small(6)

    

