def push(item): # 삽입 연산
    stack.append(item)

def peek(): # top 항목 접근
    if len(stack) != 0:
        return stack[-1]

def pop(): # 삭제 연산
    if len(stack) != 0:
        item = stack.pop(-1)
        return item

# 스택에 1, 2, 3, 4, 5의 순서로 입력이 주어질 때 push와 pop연산을 수행하여 얻을 수 있는 출력(실행하시면 됩니다.)
stack = []
stack_2 = []

push(1)
push(2)
push(3)

print('3을 pop()을 하기 전 stack:', stack)
stack_2.append(pop())
print("pop()하고 출력값:", stack_2,end='\n\n')

push(4)

print('4을 pop()을 하기 전 stack:', stack)
stack_2.append((pop()))
print("pop()하고 출력값:", stack_2,end='\n\n')

push(5)

print('5을 pop()을 하기 전 stack:', stack)
stack_2.append((pop()))
print("pop()하고 출력값:", stack_2,end='\n\n')

print('2을 pop()을 하기 전 stack:', stack)
stack_2.append((pop()))
print("pop()하고 출력값:", stack_2,end='\n\n')

print('1을 pop()을 하기 전 stack:', stack)
stack_2.append((pop()))
print("pop()하고 출력값:", stack_2,end='\n\n')

print('push, pop()하여 최종 출력된 값:', stack_2)

# 답 4번 