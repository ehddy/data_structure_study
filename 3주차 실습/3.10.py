def push(item): # 삽입 연산
    stack.append(item)

def peek(): # top 항목 접근
    if len(stack) != 0:
        return stack[-1]

def pop(): # 삭제 연산
    if len(stack) != 0:
        item = stack.pop(-1)
        return item

stack = []
stack_2 = []
i =  1
while len(stack) < 3:
    push(i)
    i += 1 
print('3을 pop()을 하기 전 stack:', stack)
stack_2.append(pop())
print("pop()하고 출력값:", stack_2,end='\n\n')

print('2를 pop()을 하기 전 stack:', stack)
stack_2.append(pop())
print("pop()하고 출력값:", stack_2,end='\n\n')

print('1을 pop()을 하기 전 stack:', stack)
stack_2.append(pop())
print("pop()하고 출력값:", stack_2,end='\n\n')

# 빈 리스트(stack)에 4, 5를 push 
push(4)
push(5)

print('5를 pop()을 하기 전 stack:', stack)
stack_2.append(pop())
print("pop()하고 출력값:", stack_2,end='\n\n')

print('4를 pop()을 하기 전 stack:', stack)
stack_2.append(pop())
print("pop()하고 출력값:", stack_2,end='\n\n')

print('push, pop()하여 최종 출력된 값:', stack_2)