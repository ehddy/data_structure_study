
# 괄호 짝 맞추기를 위한 파이썬 프로그램 구현 
def solution(parentheses):
    # pop()한 값과 비교하기 위한 사전을 생성 
    dic = {
        ')': '(',
        '}': '{'
    }
    # 괄호의 짝을 맞추는 데 사용할 빈 리스트를 생성 
    stack = []
    for i in parentheses:
        # 왼쪽 괄호는 스택에 push(만약 오른 괄호를 읽으면 pop)
        if i in '({':
            stack.append(i)
        elif i in ')}':
            if stack:
                top = stack.pop()
                # 오른쪽 괄호의 값이 pop한 왼쪽 괄호의 값과 다르면 False를 리턴하고 종료 
                if dic[i] != top:
                    return False
            # stack이 빈리스트인데 오른쪽 괄호가 나오면 False를 리턴         
            else:
                return False
    # 위에 조건을 이용하여 입력의 모든 괄호들을 False 없이 정상적으로 처리한 후에 스택의 len은 0이 된다.             
    return len(stack) == 0


print(solution('{(){()}}'))