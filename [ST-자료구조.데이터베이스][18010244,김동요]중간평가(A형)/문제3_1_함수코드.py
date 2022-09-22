class Node: # 노드 생성자 
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right 
    
    
class BST:
    def __init__(self): # 트리 생성자
        self.root = None  
 
 

    """문제설명: 최대값을 삭제하는 delete_max() 메소드를 만드는 것
    먼저 delete_max() 메소드를 만들어서 만약 root값이 없다면(노드가 없다면) 트리가 비어있다는 문자열을 출력하고
    노드가 이미 있다면 del_max() 메소드를 실행하여 리턴값을 self.root에 연결해줍니다. 
    del_max() 메소드에 대한 설명하기 전에, 이진탐색트리의 최소값은 맨 왼쪽에 있는 노드이며 최대값은 맨 오른쪽에 있는 노드라는 것을 
    이진탐색트리 규칙을 통해 알 수 있었습니다. 그래서 먼저 del_max()를 실행하여 root부터 시작하여 해당 노드(n)의 오른쪽 노드가 
    None(n은 최대값)이 될 때까지 오른쪽으로 이동하는 재귀호출을 진행합니다. 
    만약 n의 오른쪽 노드가 더 이상 없어서(None), 최대값을 찾았다면 그 최대값의 왼쪽 값을 리턴해줍니다. 그럼 반대방향으로 리턴을 진행하며 
    최대값 노드가 연결에서 제외되고 리턴된 왼쪽 노드나 빈값(왼쪽이 None 값일수도 있음)이 자연스럽게 root노드까지 연결됩니다. 
    저는 추가로 이해를 돕기 위해 최대값(key)을 리턴하는 메소드 max()도 구현해봤으며 실행파일에서 사용했습니다."""

    # 최대값을 삭제하는 메소드 구현 
    def delete_max(self):
        # 만약 root가 없다면(트리 안에 노드가 없다면) None이면 트리가 비어있다는 문자열을 출력하고 함수 종료 
        if self.root == None:
            print('트리가 비어있음')
            return None
        # 노드가 이미 있다면 del_max() 메소드를 실행하여 리턴값을 self.root에 연결 
        self.root = self.del_max(self.root) # 루트와 del_min()이 리턴하는 노드를 재 연결 


    def del_max(self, n):
        if n.right == None:
            return n.left # 최대값을 가진 노드의 왼쪽 자식이나 빈값(만약 왼쪽 자식이 None이면)을 순서대로 연결 

        n.right = self.del_max(n.right) # n의 오른쪽 자식과 del_max()이 리턴하는 노드를 재 연결 
        return n  

    
    def max(self): # 최대값 가진 노드 찾기 
        if self.root == None:
            return None
        return self.maximum(self.root).key

    def maximum(self, n):
        if n.right == None: # 오른쪽자식이 None인 노드(최대값을 가진)를 리턴 
            return n
        return self.maximum(n.right) # 오른쪽자식으로 반복해서 재귀호출   

    
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
    

    def inorder(self, n): # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key), "  ", end='') # 왼쪽 서브트리 방문 후 노드 방문 
            if n.right:
                self.inorder(n.right)



