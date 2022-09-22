class Node: # 노드 생성자 
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right 
    
    

class BST:
    def __init__(self): # 트리 생성자
        self.root = None  
        
 
  
    """ 문제설명: 이진트리가 입력으로 주어졌을 때, 입력으로 주어진 트리가 이진탐색인지 확인하는 메소드 구현
    이진 탐색 트리의 특징 중 하나가 중위 순회를 하면 정렬된 값을 출력하는 것입니다. 또한, 왼쪽의 노드는 자신보다 작은 값이고,
    오른 쪽의 노드는 자신보다 큰 값이 와야 합나다. 
    저는 처음에 중위순회를 재귀호출로 진행하여 순회를 진행하다가 이진탐색트리 조건(왼쪽노드는 작고 오른쪽 노드는 큰)에 위배가 된다면 
    이진탐색트리가 아니라는 문자열을 출력하도록 만들었지만, 만약 위배되는 노드가 2개라면 문자열이 두번이나 나오게 되는 문제가 발생했습니다.
    또한, 만약 이진탐색트리의 조건에 맞아 중간순회 값이 정렬이 나왔다면 이진탐색트리가 맞다는 것을 나타내는 문자열을 넣고 싶었지만, 재귀호출로 인해 
    무한 루프에 빠지게 되어 그것 또한, 실패했습니다.
    
    그래서 저는 중위순회를 반복문을 통한 스택형식으로 구현해봤으며 중위순회로 나오는 값들을 순차적으로 sorted_node 리스트에 넣어주었습니다.
    스택형식으로 중위순회를 반복으로 표현한 코드는 문제 3-2에서도 이용하므로, 
    이에 대한 설명은 문제3_2_함수코드 파일에서 자세히 설명되어 있으니 참고하시면 감사하겠습니다.  
    저는 중위 순회를 진행하고 난 뒤에 최종적으로 도출된 리스트(sorted_node)의 값이 정렬인지 확인하여 
    만약 sorted 메소드로 정렬시킨 리스트와 정렬하기 전에 리스트와 값이 일치한다면(if sorted(리스트) == 리스트) 
    이진탐색트리의 조건에 맞는 것이며, 만약 정렬시킨 리스트와 정렬하기 전에 리스트의 값이 다르다면 이진탐색트리 규칙에 위배가 되도록 조건문을 설정했습니다. 
    그리고 조건에 맞으면 이진탐색트리가 맞다는 문자열을 조건에 위배되면 이진탐색트리가 아니다라는 문자열을 출력해주었습니다. 
    또한 왜 이진탐색트리의 조건을 위배했는지, 아니면, 이진탐색트리에 조건에 맞는지 이해하기 쉽게 설명하기 위해, 
    해당 트리를 중위 순회한 결과를 문자열 뒤에 출력해보았습니다..  """

    def isbst(self):
        # 루트부터 진행하여 k번째로 작은 key와 value가 있는 튜플을 리턴 
        return self.isbst_yes_no(self.root)

    def isbst_yes_no(self, n): 
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
                sorted_node.append(n.key)
                n = n.right
        # 정렬된 sorted_node에서 k번째로 작은 값을 리턴()
        if sorted(sorted_node) == sorted_node:
            print('이진탐색트리입니다.')
            print('중위순회 했을 때 정렬: ', end="  ")
            self.inorder(self.root)
            print(end='\n\n')
        else:
            print('이진탐색트리가 아닙니다.')   
            print('중위순회했을 때 정렬되어 있지 않음: ', end="  ")
            self.inorder(self.root)
            print(end='\n\n')
        


    def inorder(self, n): # 중위순회    
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(str(n.key), "  ", end='') # 왼쪽 서브트리 방문 후 노드 방문 
            if n.right:
                self.inorder(n.right)

   
            
        
    
            

   
  

   