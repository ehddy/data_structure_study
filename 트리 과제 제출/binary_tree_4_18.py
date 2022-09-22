class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self): # 트리 생성자 
        self.root = None # 트리의 루트 

    
    def preorder(self, n): # 전위순회
        if n != None:
            print(str(n.item), ' ', end='') # 맨 먼저 노드 방문 
            if n.left:
                self.preorder(n.left) # 왼쪽 서브트리 방문 후, 오른쪽 서브트리 방문 
            if n.right:
                self.preorder(n.right)   
        
    def inorder(self, n): # 중위순회
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item), "  ", end='') # 왼쪽 서브트리 방문 후 노드 방문 
            if n.right:
                self.inorder(n.right)
    
    def postorder(self, n): # 후위순회 
        if n != None: # 왼쪽과 오른쪽 서브트리 모두 방문 후 노드 방문 
            if n.left: 
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item), ' ', end='')

    def levelorder(self, root): # 레벨순회
        q = [] # 리스트로 큐 자료구조 구현 
        q.append(root)
        while len(q) != 0:
            t = q.pop(0) # 큐에서 첫 항목 삭제
            print(str(t.item), ' ', end='') # 삭제된 노드 방문 
            if t.left != None: # 왼쪽자식, 오른쪽자식 큐에 삽입 
                q.append(t.left)
            if t.right != None:
                q.append(t.right)
    
    def height(self, root): # 트리 높이 계산 
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1 


    # 이진트리의 동일성 검사
    # 2개의 트리의 동일성 여부를 확인하는 메소드. \
    # n은 m은 각 트리의 root이고 root부터 시작하여 재귀호출을 통해 각각 노드 값을 비교
    # 동일하면 True, 불일치 하면 False를 리턴 
    def q(self, n, m):
        if n == None or m == None:
            return n == m
        if n.item != m.item:
            return False

        return(self.q(n.left, m.left) and self.q(n.right, m.right))
    
