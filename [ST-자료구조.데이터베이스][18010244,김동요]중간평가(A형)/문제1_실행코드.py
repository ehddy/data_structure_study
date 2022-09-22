from 문제1_함수코드 import BST, Node 
if __name__ == '__main__':
  # 이진 탐색 트리가 아닌 경우(문제 1의 1번 그림)
    non_bst = BST()
    a = Node(50, 'A')
    b = Node(30, 'B')
    c = Node(80, 'C')
    d = Node(10, 'D') 
    e = Node(20, 'E')
    f = Node(90, 'F')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    non_bst.root = a

  # 이진 탐색 트리일 경우(문제 1의 3번 그림)
    yes_bst = BST()
    a = Node(40, 'A')
    b = Node(30, 'B')
    c = Node(60, 'C')
    d = Node(10, 'D') 
    e = Node(90, 'E')

    a.left = b
    a.right = c
    b.left = d
    c.right = f
    yes_bst.root = a

    # 이진탐색트리인지 학인하는 메소드 실행 
    
    # 이진 탐색 트리가 아닐경우 
    print("#1")
    non_bst.isbst()

    # 이진 탐색 트리일 경우 
    print("#2")
    yes_bst.isbst()

