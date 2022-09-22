# 입력: 옮기려는 원반의 개수 x 
# 옮길 원반이 현재 있는 출발점 기둥 from_pillar
# 원반을 옮길 도착점 기둥 to_pillar 
# 옮기는 과정에서 사용할 보조 기둥 assi_pillar
# 출력: 원반을 옮기는 순서 

def hanoi(n, from_pillar, to_pillar, assi_pillar):

        if n == 1: # 원반을 한 개만 옮긴다면 그냥 옮기면 됨 
            print(from_pillar, '->', to_pillar)
            return # return값이 없다면 함수를 종료

        # 원반 n-1개를 assi_pillar로 이동(to_pillar를 보조 기둥으로)
        hanoi(n - 1, from_pillar, assi_pillar, to_pillar)
        
        # 가장 큰 원반을 목적지로 이동 
        print(from_pillar, '->', to_pillar)
        
        # assi_pillar에 있는 원반 n - 1개를 목적지로 이동(from_pillar를 보조 기둥으로)
        hanoi(n - 1, assi_pillar, to_pillar, from_pillar)
    
print('n = 1')
hanoi(1, 1, 3, 2) # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)

print('\nn = 2')
hanoi(2, 1, 3, 2) # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)

print('\nn = 3')
hanoi(3, 1, 3, 2)  # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동(2번 을 보조 기둥으로)