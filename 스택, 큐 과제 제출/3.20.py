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

# 중위 표기법 -> 후위 표기법 변환 
# 1. 수식의 각 연산자에 대해 우선순위에 따라 괄호를 사용하여 다시 표현
# 2.각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동시킨다.
# 3. 괄호를 제거

# 알고리즘 설계 
def Convert(express_list):

    # 연산자 우선순위를 부여하기 위한 사전을 생성 
    opre = {
        '*':4,
        '/':4,
        '+':3,
        '-':3,
        '(':1,
    }

    # 후위 표현식으로 만들어져 반환될 리스트 생성 
    result_list = []

    # 중위 표현식을 왼쪽부터 한글자씩 읽음
    for express in express_list:

        # 피연산자면 리스트에 append
        if type(express) is int:
            result_list.append(express)

        # 연산자면 스택에서 이보다 높은 우선순위들 POP, 리스트에 append
        elif express == ')':
            while peek() != '(':
                result_list.append(pop())
            pop()
        else:
            if len(stack) > 0:

                # 연산자면 스택에서 이보다 높은 우선순위들 POP, 리스트에 append
                if opre[peek()] >= opre[express] and express != '(':
                    result_list.append(pop())
                    push(express)

                # '('이면 스택에 push
                else:
                    push(express)
            else:
                push(express)
    # 스택에 남아있는 연산자는 모두 POP, 리스트에 append
    while len(stack) != 0:
        result_list.append(pop())       

    return result_list

# 후위 표기법 계산
# 1. 처음부터 차례대로 읽으며 피연산자는 스택에 쌓음 
# 2. 연산자를 만나면 스택에서 피연산자 2개를 꺼내 연산을 수행하고 다시 스택에 쌓음
# 3. 모두 읽을 때 까지 위 두 공식을 반복

# 알고리즘 설계
def Calculate(express_list):

    # 후위 표현식을 왼쪽부터 한 글자씩 읽음 
    for express in express_list:

        # 피연산자면 스택에 push
        if type(express) is int:
            push(express)
        
        # 연산자면 스택에서 pop해서 express_1, 다시 pop해서 express_2에 저장 
        # 두 변수를 연산자로 계산하여, 결과값 스택에 push
        elif express == '*':
            express_1 = pop()
            express_2 = pop()
            push(express_1*express_2)
        elif express == '/':
            express_1 = pop()
            express_2 = pop()
            push(express_1/express_2)
        elif express == '+':
            express_1 = pop()
            express_2 = pop()
            push(express_1+express_2)
        elif express == '-':
            express_1 = pop()
            express_2 = pop()
            push(express_1-express_2)
    # 수식의 끝이면 스택에서 pop하여 계산 결과 도출 
    return pop()


convert = Convert(['(', 1, '+', 3, ')', '*', '(', 2, '+', 3, ')'])
print('후위표기법으로 변환된 값:', convert)
calculate = Calculate(convert)
print('후위표기법으로 된 수식 계산 값:', calculate)




