"""
호프만 코드는 데이터를 효율적으로 압축하는데 사용하는 방법으로 탐욕 알고리즘 중 하나
압축하고자 하는 문자열에서 자주 등장하는 문자는 짧은 비트로 표현하고 
거의 등장하지 않는 문자는 긴 비트로 표현(가변 길이 코드)
즉, 문자의 빈도수를 이용

우선 허프만 코드를 만들기 위해 트리를 만들어야 한다
빈도수를 비교하여 가장 작은 빈도수를 가진 노드와 두 번째로 작은 빈도수를 가진 것을 찾아서 두 개의 빈도수를 합친 수로 노드를 하나 만들어 준다.
그리고 만들어준 노드의 왼쪽 자식에는 가장 작은 빈도 수의 노드를 연결하고 오른쪽 자식에는 두 번째로 작은 빈도수를 가진 노드를 연결한다. 
이를 반복하여 비교할 노드가 한 개가 남을 때까지 반복
완성한 트리 노드의 왼쪽 간선에는 0, 오른쪽 간선에는 1 가중치를 둔다. 
트리들의 단 노드가 압축하고자 하는 문자가 되며 그 문자들을 루트로부터 탐색했을 때 지난 간선들의 가중치들의 합이 허프만 코드(가변 길이 코드)가 된다.
인코딩은 문자열들의 문자를 구한 허프만 코드로 치환해주면 된다.
디코딩도 완성된 트리를 사용해서 하는데 인코딩된 문자열들을 앞에서부터 읽어들여 root 노드로부터 0이 나오면 왼쪽 자식으로 이동하고 
1이 나오면 오른쪽 자식으로 이동하여 단 노드가 나올때까지 이를 반복
"""
# 클래스 생성 
class HuffNode:
    # string은 문자, freq는 빈도 수 
    def __init__(self, string, freq):
        self.string = string
        self.freq = freq
        self.left = None
        self.right = None 
        self.lefts = "0"
        self.rights = "1"
    
    def preorder(self): # 전위 순회
        print(self.freq, end=" ")
        if (self.left is not None):
            self.left.preorder()
        if (self.right is not None):
            self.right.preorder()
    
    def inorder(self): # 중위 순회
        if (self.left is not None):
            self.left.inorder()
        print(self.freq, end=" ")
        if (self.right is not None):
            self.right.inorder()

# n = 주어진 파일내 문자의 개수 
def huffman(n, PQ):
    for _ in range(n - 1):
        p = PQ.get()[1]
        q = PQ.get()[1]
        r = HuffNode(' ', p.freq + q.freq)
        r.left = p
        if r.left != None:
            r.lefts  += "0"
        r.right = q 
        if r.right != None:
            r.rights += "1"
        PQ.put((r.freq, r)) 
    return PQ.get()[1]

codes = ['b', 'e', 'c', 'a', 'd', 'f']
freqs = [5, 10, 12, 16, 17, 25]

from queue import PriorityQueue

PQ = PriorityQueue()

for i in range(len(codes)):
    node = HuffNode(codes[i], freqs[i])
    PQ.put((node.freq, node))

root = huffman(len(codes), PQ)

# a = ""
# for i in range(root):
#     if root[i].lefts != None:
#         a += root[i].lefts
#     if root[i].rights != None:
#         a += root[i].rights
# a = ""
# while root.left or root.right:
#     a += root.lefts 
#     a += root.rights 
#     root = root.left
#     root = root.right 

# print(a)
        

print('Preorder:', end=' ')
root.preorder()
print('\nInorder', end=' ')
root.inorder()
print()

"""이진 트리로 허프만 코드의 트리를 만드는 것과
전위순회, 중위순회로 노드를 출력하는 것은 성공했지만, 
노드의 왼쪽 레퍼런스에 0을 오른쪽 레퍼런스에 1의 가중치를 
주는 코드를 완성하지 못했습니다... 수업시간에 상세한 설명 부탁드립니다.
탐색을 해서 출력을 해야될 거 같은데 이진트리의 탐색을 하는 코드를 모르겠습니다"""

