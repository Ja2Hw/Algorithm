# 2621 카드게임
# 실버 3

import sys
input = sys.stdin.readline

score = 0
color = []
num = []

for _ in range(5):
    c, n = input().split()
    color.append(c)
    num.append(int(n))

num.sort()

color_set = list(set(color))
num_set = list(set(num))

# 스트레이트 확인 함수
def check(num):
    if len(num) == 5 and num[4]-num[3] == num[3]-num[2] == num[2]-num[1] == num[1]-num[0] == 1:
        return True
    else:
        return False

# 플러시
if len(color_set) == 1:
    # 숫자가 연속적일 때
    if check(num):
        score = max(score, max(num)+900)
    # 색깔만 같을 때
    else:
        score = max(score, max(num)+600)

# 포카드 or 풀하우스
elif len(num_set) == 2:
    # 포카드
    if num.count(num_set[0]) == 4:
        score = max(score, num_set[0]+800)
    elif num.count(num_set[1]) == 4:
        score = max(score, num_set[1]+800)
    # 풀하우스
    elif num.count(num_set[0]) == 3:
        score = max(score, num_set[0]*10 + num_set[1]+700)
    else:
        score = max(score, num_set[1]*10 + num_set[0]+700)

# 트리플 or 투페어
elif len(num_set) == 3:
    tmp = []
    for k in num_set:
        # 트리플
        if num.count(k) == 3:
            score = max(score, k+400)
            break
        # 투페어
        elif num.count(k) == 2:
            tmp.append(k)
    else:
        score = max(score, max(tmp)*10+min(tmp)+300)

# 원페어
elif len(num_set) == 4:
    for k in num_set:
        # 5장 중 2장이 같을 때
        if num.count(k) == 2:
            score = max(score, k+200)
            break

# 스트레이트 or 하이카드
elif len(num_set) == 5:
    # 스트레이트
    if check(num):
        score = max(score, max(num)+500)
    # 하이카드
    else:
        score = max(score, max(num)+100)

# 점수 출력
print(score)
