
# 문제 설명: 
# N x N 2차원 리스트 a에서 a[0][0]에서 a[N-1][N-1]까지 경로를 찾기 위해 스택을 이용한 파이썬 프로그램 작성
# 리스트 a의 원소는 0 또는 1을 가지며, 0은 통과 가능한 열린 공간이고 1을 통과할 수 없는 블록 
# 경로는 리스트의 한 원소에서는 상하좌우 방향으로만 진행 가능 
# N은 5와 50사이의 양수 

# 기본 스택 함수를 파이썬으로 구현 
stack = []

def push(item): # 삽입 연산
    stack.append(item)

def peek(): # top 항목 접근
    if len(stack) != 0:
        return stack[-1]

def pop(): # 삭제 연산
    if len(stack) != 0:
        item = stack.pop(-1)
        return item

# 미로의 탈출 유뮤와 이동 횟수(경로)를 탐색하는 함수 
def Maze_Solution(N): 
    # 이동 방향 경우의 수 모두 생성 
    move = [(1, 0), (-1,0), (0, 1), (0, -1)]

    # N X N 2차원 리스트 생성 
    maze_list = [list(map(int, list(input()))) for _ in range(int(N))]

    # 첫 인덱스 값    
    x, y = 0, 0

    # 미로 탈출 여부 
    result = '실패'

    # 경로까지 가기 위한 이동 횟수 
    try_iter = 1

    # 스택에 저장 
    push((x, y))

    # 스택이 빌때까지 반복 
    while stack:
    # 스택에 있는 값을 꺼내서 
        x, y = pop()
        
        # 현재 위치는 이동할 예정이니 1로 변경 
        maze_list[x][y] = 1 
        
        # 이동할 4방향을 검사 
        for _x, _y in move:
            dx = x + _x
            dy = y + _y

            # 바운드리(제약) 설정
            if dx < 0 or dy < 0 or dx >= N or dy >= N:
                continue

            # 현재 인덱스의 값이 N-1 N-1이면 도착 지점(미로 탈출 성공)
            if dx == N-1 and dy == N-1:
                
                # 결과 변경후 반복문 종료
                result = "성공"
                break

            # 0이라면 갈 수 있는 장소이니 스택에 추가
            elif maze_list[dx][dy] == 0:
                push((dx, dy))
                try_iter += 1
                    
            else:
                # 브레이크 없이 끝났다면 다음 것으로 진행
                continue
    # 최종적으로 탈출 유무와 이동 횟수 출력 
    print('{}번 이동하여 미로 탈출을 {}했습니다.'.format(try_iter, result))

"""함수 사용법은 먼저 원하는 미로의 크기를 파라미터(N)로 주고 
직접 미로의 내부 값을 입력한다.  
입력 예시:
001
010
000 
주의사항: 내부 값은 0과 1만 입력, 
N은 5와 50 사이에 양수로 입력할 것,
0은 통과가 가능한 열린 공간이고, 1은 통과할 수 없는 블록"""

# 실습 예시 
Maze_Solution(3) # 3 X 3의 미로를 생성하여 탈출 가능 유뮤를 출력해줌(미로 내부값은 직접 입력(input)) 




