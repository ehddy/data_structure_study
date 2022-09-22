class Node:
    def __init__(self, item):
        self.data = item
        self.next = None 

# 정렬된 단순연결리스트를 순서대로 병합 
class Solution: 
    def merge_sort_Lists(self, l1: Node, l2: Node):
            # 아무 값도 없는 dummy노드를 생성 
        current_node = Node(None) # (0, None)
            # dummy노드를 새로운 변수에 저장 
        return_node = current_node
        
        while l1:
            a = l2 
            while l2:
                if l1.data == l2.data:
                    current_node.next = Node(l1.data + l2.data) 
                    current_node = current_node.next 
                l2 = l2.next
            l1 = l1.next 
            l2 = a 
        return return_node.next
# l1를 생성 
l1 = Node(3) 
l1.next = Node(4)
l1.next.next = Node(5)

# l2를 생성 
l2 = Node(4)
l2.next = Node(5)
l2.next.next = Node(6)

# 노드들의 병합을 프린트 하는 코드 
d = Solution()

lists = d.merge_sort_Lists(l1, l2)
if lists:
    a = 0
    while lists:
        a += lists.data
        lists = lists.next
    print("공통된 값들의 합:", a)
else:
    print("공통된 값 없음")

