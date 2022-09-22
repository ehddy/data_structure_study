class Node: # 노드 생성자 
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right 
    
    

class BST:
    def __init__(self): # 트리 생성자
        self.root = None  
    

    """문제 설명: 반복문을 이용하여 이진탐색트리 삽입 연산 메소드를 만드는 것 
    put_loop_run 메소드를 만들어 파라미터로, 삽입할 노드의 key와 value를 넣었습니다. 
    
    조건1 :만약 노드의 root 값이 없다면(아무 노드도 없을 경우) 
    루트에 새로운 노드를 넣어줍니다. 그리고 n에 새로 생성한 루트를 넣어서 그대로 리턴합니다.
    
    조건2: 이미 노드가 있을 경우 
    기존 노드의 root를 변수 n에 저장하고 n의 key와 새롭게 삽입할 노드의 key와 비교를 진행하면서 조건에 따라
    n을 이동시킵니다. 하지만 n을 이동시키기 전에 다음으로 이동할 노드가 빈 값이라면 그 위치에 새롭게 입력한 노드를 삽입시켜줍니다. 
    삽입한 후에 이동을 시켜주고 그 상태로 n을 리턴합니다. 만약 이동한 값이 빈값이 아니라면 리턴을 하지 않고 n만 조건에 맞게 이동해줍니다. 
    비교를 진행하는 이유는 이진 탐색트리는 항상 현재 노드의 왼쪽에는 작은 값이 오른쪽에는 큰값이 와야 하는 규칙이 있기 때문입니다. 
    그래서 넣어줄 새로운 노드의 key가 만약 현재 노드 보다 작다면 왼쪽으로 가야하고 크다면 오른쪽으로 가서 삽입되어야 됩니다. """
    
    # 반복문 삽입 구현 메소드 
    # 파라미터로 삽입할 key와 value를 넣어줌    
    def put_loop_run(self, key, value):
        # 조건1: 만약 노드의 root가 없다면 
        if self.root == None:
            # 루트에 노드를 넣어줌 
            self.root = Node(key, value)
            n = self.root
            # 하당 루트 값을 리턴하고 함수 종료 
            return n
        # 조건 2: 이미 트리에 노드가 1개 이상 존재한다면 
        # root를 변수 n에 저장 
        n = self.root 
        while n:
            if n.key > key:
                # 만약 이동할 위치가 비어있다면 그 이동할 자리에 새로운 노드를 삽입 
                if n.left == None:
                    n.left = Node(key, value)
                    # 이동할 자리에 새로운 노드를 삽입한 후에 이동을 실시 
                    n = n.left 
                    # 새로운 노드를 갖게 된 n을 리턴하고 함수 종료 
                    return n 
                # 만약 이동할 위치에 이미 노드가 있다면 삽입을 하지 않고 그 자리로 이동 
                # 빈값이 나올때까지 반복해서 이동 
                n = n.left          
            
            # 위와 반대 조건으로 진행(오른쪽으로 이동)
            elif n.key < key:
                if n.right == None:
                    n.right = Node(key, value)
                    n = n.right 
                    return n 
                n = n.right
            
            # 만약 key값이 같을 경우 key값을 그대로 냅두고 value값만 바꿔줌 
            else:
                n.value = value 
                return n 

    def inorder(self, n): # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key), "  ", end='') # 왼쪽 서브트리 방문 후 노드 방문 
            if n.right:
                self.inorder(n.right)

    