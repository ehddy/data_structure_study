from 문제3_1_함수코드 import BST
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

    # 최대값을 몇인지 max()로 확인 
    print('최대값 : {}'.format(t.max()))
    print('최대 값 삭제 전 중위 순회: ')
    
    # 최대값을 삭제하기 전에 중위 순회 확인 
    t.inorder(t.root)
    print()  
    print('\n최대값({}) 삭제 후 중위 순회: '.format(t.max()))
    
    # 최대값을 삭제하는 메소드 실행 
    t.delete_max()
    # 최대값을 삭제한 후 중위순회 
    t.inorder(t.root)