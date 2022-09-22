from 문제2_1_함수코드 import BST, Node 
if __name__ == '__main__':
    t = BST()
    # 노드 삽입 
    t.put(10, 'A')
    t.put(5, 'B')
    t.put(15, 'C')
    t.put(3, 'D')
    t.put(8, 'E')
    t.put(13, 'F')
    t.put(18, 'G')

    # 더욱 간편하게 출력하기 위해 새로운 함수를 만들어서 key와 value값을 둘 다 출력 
    # n에는 value값을 알고싶은 key값을 넣어줌 
    def get_key_value(n):
        # 찾고 싶은 key 값을 입력하여 만약 탐색에 성공했다면 해당 value값이 변수에 저장되고 탐색에 실패했다면 실패했다는 문자열이 저장  
        value = t.get_loop(n) # 함수를 실행해서 나온 값을 변수에 저장 
        print('내가 찾는 key({})의 value는 {}'.format(n, value))

    # 함수실행   
    get_key_value(10)

    


