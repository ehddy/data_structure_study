class Node: # 노드 생성자 
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right 
    
    

class BST:
    def __init__(self): # 트리 생성자
        self.root = None  

    
    """문제설명 : 이진탐색트리에서 k번째 작은 키를 찾는 kth_smallest() 메소드를 구현하는 것 
    kth_smallest 메소드는 kth_smallest_search 메소드를 실행한 뒤, 노드의 root부터 탐색을 시작하여 k번째로 작은 값을 리턴하는 메소드입니다. 
    기존에는 중위순회를 이용하여 k번쨰로 나온 값을 리스트에 추가해서 구하려 했지만 재귀호출을 하게 되면 리스트가 초기화되는 현상이 발생하여 
    중위순회를 재귀호출이 아닌 반복문을 이용하여 스택형식(한 쪽 끝에서만 항목을 삭제하거나 추가하는 자료구조)으로 구현해봤습니다. 
    면저 노드의 root를 변수 n에 저장하고 2개의 리스트를 생성합니다. sorted_node는 저희가 최종적으로 구할 정렬된 리스트며 stack(리스트)은
    pop을 진행하여 pop한 값을 sorted_node에 append하는 역할을 합니다.
    반복문은 n과 stack 둘다 None이 되었을 때 종료합니다(더이상 pop할 값이 없고 stack에 추가할 값(n)이 없을 때)
    먼저 반목문 안에 있는 조건은 중위순회의 조건을 따라야 하며, 그 이유는 중위 순회의 순서로 sorted_node의 순서에 따라야 이진탐색트리의 
    조건을 만족하기 때문입니다. 먼저 n이 none값이 아닐경우 stack에 append를 해주고 왼쪽으로 노드를 이동시켜줍니다. 만약 더이상 왼쪽이 없다면
    (n이 None, 하지만 stack에는 값이 있으니 반복) else의 조건에 따라 스택에 있는 값을 pop(끝값을 삭제)하여 그 값을 sorted_node에 
    append 시켜 줍니다. 그리고 나서 노드를 오른쪽으로 이동시키는데 만약 오른쪽 값(n)이 None이라면 또다시 else문을 반복적으로 진행해줍니다.
    왼쪽을 전부 이동한 후 맨 왼쪽부터 하나하나씩  값을 넣어주고 나서 만약 오른쪽 노드가 나온다면 이동해준다음에 제가 위에서 설명한 방식으로 
    n과 stack이 None이 될 때(중위 순회 끝)까지 반복해줍니다. 반복문이 끝나고 나면 내가 찾기 원하는 k번째로 작은 key는 중위순회 형식으로
    저장되어 정렬되어 있는 sorted_node의 k번째, 즉 sorted_node[k]가 됩니다. sorted_node[k]를 리턴해주고 함수를 종료합니다.
    저는 추가로 key와 value도 튜플형식으로 같이 구해보았습니다"""
    
    def kth_smallest(self, k):
        # 루트부터 진행하여 k번째로 작은 key와 value가 있는 튜플을 리턴 
        return self.kth_smallest_search(self.root, k)

    def kth_smallest_search(self, n, k): 
        # n에 노드의 root를 저장(루트부터 중위순회를 진행)
        n = self.root 
        sorted_node = []
        stack = []

        while stack or n: # n과 stack 둘다 None이 되었을 때 종료(더이상 pop할 값이 없고 stack에 추가할 값(n)이 없을 때
            # 만약 n이 있으면 stack에 넣어준 뒤 왼쪽으로 이동(왼쪽부터 확인하고 오른쪽을 확인: 중위순회) 
            if n:
                stack.append(n)
                n = n.left
            # 만약 n이 없으면 stack에 있는 pop한 값을 sorted_node에 append 그리고 오른쪽으로 이동
            # (만약 오른쪽이 None이면 다시 else문 진행)
            else:
                n = stack.pop()
                # key와 value를 튜플형식으로 추가해줌 
                sorted_node.append((n.key, n.value))
                n = n.right
        # 정렬된 sorted_node에서 k번째로 작은 값을 리턴()
        return sorted_node[k]
    
   
    
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

    