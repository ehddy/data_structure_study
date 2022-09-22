class Node: # 노드 생성자 
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right 
    
    

class BST:
    def __init__(self): # 트리 생성자
        self.root = None  
    
    def preorder(self, n): # 전위순회
        if n != None:
            print(str(n.key), ' ', end='') # 맨 먼저 노드 방문 
            if n.left:
                self.preorder(n.left) # 왼쪽 서브트리 방문 후, 오른쪽 서브트리 방문 
            if n.right:
                self.preorder(n.right)   
        
    def inorder(self, n): # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key), "  ", end='') # 왼쪽 서브트리 방문 후 노드 방문 
            if n.right:
                self.inorder(n.right)
    
    def postorder(self, n): # 후위순회 
        if n != None: # 왼쪽과 오른쪽 서브트리 모두 방문 후 노드 방문 
            if n.left: 
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.key), ' ', end='')
    
    def get(self, k): # 탐색 연산 
        return self.get_item(self.root, k)

    def get_item(self, n, k):
        if n == None: # 탐색 실패
            return None
       
        elif n.key > k:   # k가 노드의 key보다 작으면 왼쪽 서브 트리 탐색 
            return self.get_item(n.left, k)
      
        elif n.key < k:  # k가 노드의 key보다 크면 오른쪽 서브 트리 탐색 
            return self.get_item(n.right, k)
        
        else:
            return n.value # 탐색 성공 

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

    def min(self): # 최솟값 가진 노드 찾기 
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None: # 왼쪽자식이 None인 노드(최솟값을 가진)를 리턴 
            return n
        return self.minimum(n.left) # 왼쪽자식으로 재귀호출하며 최솟값 가진 노드를 리턴 


    def delete_min(self): # 최솟값 삭제
        if self.root == None:
            print('트리가 비어있음')
        
        self.root = self.del_min(self.root) # 루트와 del_min()이 리턴하는 노드를 재 연결 

    
    def del_min(self, n):
        if n.left == None:
            return n.right # 최솟값을 가진 노드의 오른쪽 자식을 리턴 

        n.left = self.del_min(n.left) # n의 왼쪽 자식과 def_min()이 리턴하는 노드를 재 연결 
        return n  


    def delete(self, k):
        self.root = self.del_node(self.root, k) # 루트와 del_node()가 리턴하는 노드를 재연결 

    def del_node(self, n, k):
        if n == None:
            return None
        if n.key > k:
            n.left = self.del_node(n.left, k) # n의 왼쪽 자식과 del_node()가 리턴하는 노드를 재연결 
        elif n.key < k:
            n.right = self.del_node(n.right, k) # n의 오른쪽 자식과 del_node()가 리턴하는 노드를 재연결 

        else:
            if n.right == None:
                return n.left 
            if n.left == None:
                return n.right 

            target = n  # target은 삭제될 노드 
            n = self.minimum(target.right) # target은 중위 후속자를 찾아 n이 참조하게 함 
            n.right = self.del_min(target.right) # n의 오른쪽 자식과 target의 오른쪽 자식 연결 
            n.left = target.left # n의 왼쪽 자식과 target의 왼쪽 자식 연결 
        return n 
    