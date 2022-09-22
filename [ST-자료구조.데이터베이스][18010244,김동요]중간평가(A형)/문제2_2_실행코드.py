from 문제2_2_함수코드 import BST, Node 
if __name__ == '__main__':
    t = BST()  

    # 반복문으로 구현한 삽입 메소드 실행 
    t.put_loop_run(500, 'apple')
    t.put_loop_run(700, 'banana')
    t.put_loop_run(200, 'melon')    
    t.put_loop_run(100, 'orange')
    t.put_loop_run(400, 'lime')
    t.put_loop_run(250, 'kiwi')
    t.put_loop_run(150, 'grape')
    t.put_loop_run(800, 'peach')
    t.put_loop_run(600, 'cherry')
    t.put_loop_run(50, 'pear')
    t.put_loop_run(350, 'lemon')
    t.put_loop_run(10, 'plum')


    # 삽입과 노드 연결이 잘 되었나 확인 
    print('이진 탐색 트리의 루트: key = {}, value = {}'.format(t.root.key, t.root.value))      

    # 이진 탐색 트리 조건에 맞게 삽입되었는지(중위순회를 하면 정렬된 값이 나와야 함) 증명 
    print('중위 순회 했을 때 정렬된 key :', end='   ')
    t.inorder(t.root)
    


