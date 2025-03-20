# 32205 네모의 꿈
# 실버 4

import sys

def sq_check(tri):
    # 각 변의 길이를 키로 하는 해시맵을 생성
    # 값은 해당 변을 가진 삼각형들의 다른 두 변의 길이 쌍을 저장
    edge = {}
    
    for a, b, c in tri:
        if a not in edge:
            edge[a] = []
        if b not in edge:
            edge[b] = []
        if c not in edge:
            edge[c] = []
        
        edge[a].append((b, c))
        edge[b].append((a, c))
        edge[c].append((a, b))
    
    # 각 변 길이에 대해 확인
    for edge_length, triangle_side in edge.items():
        # 같은 길이의 변을 가진 삼각형이 2개 이상인 경우에만 확인
        if len(triangle_side) >= 2:
            for i in range(len(triangle_side)):
                for j in range(i + 1, len(triangle_side)):
                    side1, side2 = triangle_side[i]
                    side3, side4 = triangle_side[j]
                    
                    # 삼각형을 붙였을 때 사각형이 될 수 있는지 검사
                    # 삼각형 부등식을 활용하여 사각형이 될 수 있는지 확인
                    # 네 변의 길이를 a, b, c, d라 할 때, 
                    # 가장 긴 변 < 나머지 세 변의 합이어야 사각형 형성 가능
                    sides = [side1, side2, side3, side4]
                    sides.sort()
                    
                    if sides[3] < sides[0] + sides[1] + sides[2]:
                        return True
    
    return False


n = int(sys.stdin.readline())

tri = []

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    tri.append((a, b, c))

# 결과 출력
if sq_check(tri):
    print(1)
else:
    print(0)
