# 1475 방 번호
# 실버 5

import sys

n = sys.stdin.readline().strip()

# 0부터 9까지의 숫자 개수를 저장할 리스트
count = [0] * 10

# 각 숫자 개수 세기
for digit in n:
    count[int(digit)] += 1

# 6과 9는 서로 뒤집어서 사용할 수 있으므로 합쳐서 계산
# 합친 개수를 2로 나누고 올림 처리 (홀수인 경우 올림)
count[6] = (count[6] + count[9] + 1) // 2
count[9] = 0  # 9는 6으로 합쳤으므로 0으로 설정

# 필요한 세트의 개수는 가장 많이 필요한 숫자의 개수
print(max(count))


# 첫 접근
# import sys

# n = list(sys.stdin.readline().strip())

# if '9' in  n:
#     for _ in range(n.count('9')):
#         n.append('6')
#         n.remove('9')       

# print(n)

# tmp = list(set(n))

# res = 0

# for i in tmp:
#     res = max(res, n.count(i))
    
# print(res)