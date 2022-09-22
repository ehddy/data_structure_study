class Node:
    def __init__(self, item):
        self.data = item
        self.next = None 

# 정렬된 2개의 단순 연결리스트가 가지고 있는 공통된 숫자의 합을 계산하는 함수
class Solution: 
    def merge_sort_Lists(self, l1: Node, l2: Node):
        # 아무 값도 없는 dummy노드를 생성 
        current_node = Node(None) # (0, None)
        
        # dummy노드를 새로운 변수에 저장 
        return_node = current_node
        
        # l1가 아무 값도 없을 때 까지 반복 
        # l1을 먼저 고정하고 l2 전체와 비교 -> l1을 하나 이동하고 l2 전체와 비교 -> 만약 중복된 값이 발생한 다면 둘의 합을 리스트에 넣어준다. 
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
l2 = Node(2)
l2.next = Node(3)
l2.next.next = Node(6)

# 실습 예제 코드 (바로 실행시키면 됩니다.)
d = Solution()

# 중복된 값의 합을 저장한 연결리스트를 하나씩 찾아보면서 이전 값을 더해준다. 
# 중복된 값이 2개 이상일 때도 가능함 
lists = d.merge_sort_Lists(l1, l2)
if lists:
    a = 0
    while lists:
        a += lists.data
        lists = lists.next
    print("공통된 값들의 합:", a)
else:
    print("공통된 값 없음")

