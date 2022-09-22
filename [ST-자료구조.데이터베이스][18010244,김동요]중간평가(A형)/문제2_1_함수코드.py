class Node: # 노드 생성자 
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right 
    
    

class BST:
    def __init__(self): # 트리 생성자
        self.root = None  
    

    """문제 설명: 반복문을 이용하여 이진탐색트리 탐색 연산 메소드를 만드는 것 
    이진 탐색 트리의 조건을 이용하여 매우 간단히 풀 수 있었습니다. 
    먼저, 루트부터 탐색을 시작하고 간편성을 위해 get_loop메소드의 파라미터로 k(key값)을 입력하면 루트부터 탐색을 진행하여 입력한
    key와 일치하는 value를 탐색합니다.

    먼저 이진탐색트리는 자신의 왼쪽 노드에는 현재 노드의 키보다 작은 값이 자신의 오른쪽 노드에는 현재 노드의 키보다 큰 값이 들어갑니다. 
    그래서 n이 none이 되거나(해당 key가 현 트리에는 없음) 탐색하려는 k(key)와 일치하는 노드를 찾을 때(탐색 성공)까지 
    반복문을 진행하여 현재 노드가 k(key)보다 값이 크면 왼쪽으로 현재 노드가 k(key)보다 크면 오른쪽으로 이동하며 
    만약 현재 노드의 key값이 k와 일치한다면 해당 노드의 value 값을 리턴해줍니다. 하지만, 만약 일치하는 값이 없어서 n이 끝까지 이동하다가
    n이 None이 된다면 찾는 값이 없다는 문자열을 return하여 함수를 종료시킵니다. """
    def get_loop(self, k): # 탐색 연산 
        # 함수의 root부터 탐색 시작 
        return self.get_loop_search(self.root, k)
    
    def get_loop_search(self, n, k):
        # 값을 찾지 못하고 이동하다가 None이 된다면 출력한 문자열 
        no = '존재하지 않습니다.'
        while True:
            # 현재 노드가 k(key)보다 값이 크면 왼쪽으로 이동 
            if n.key > k: 
                n = n.left 
                # 만약 이동했는데 현재 n이 None이 되었을 경우(탐색 실패한 경우)
                if n == None:
                    # 찾는 값이 없다는 문자열을 리턴하고 함수 종료 
                    return no 
            # 현재 노드가 k(key)보다 크면 오른쪽으로 이동
            elif n.key < k:
                n = n.right 
                # 만약 이동했는데 현재 n이 None이 되었을 경우(탐색 실패한 경우)
                if n == None:
                     # 찾는 값이 없다는 문자열을 리턴하고 함수 종료 
                    return no 
            # 만약 현재 노드의 key값이 k와 일치한다면 해당 노드의 value 값을 리턴
            else:
                return n.value 
   
 
    def put(self, key, value): # 삽입 연산 
        self.root = self.put_item(self.root, key, value) # 루트와 put-item()이 리턴하는 노드를 재연결 
        
    
    def put_item(self, n, key, value):
        if n == None:
            return Node(key, value) # 새 노드 생성 
        
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        elif n.key < key:
            n.right = self.put_item(n.right, key, value)
        
        else:
            n.value = value # key가 이미 있으므로 value만 갱신 

        return n 
