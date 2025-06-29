# 14468 소가 길을 건너간 이유 2
# 실버 4

import sys
input = sys.stdin.readline

cow = input().strip()

cow_index = { chr(ord('A')+i): [] for i in range(26) }
for idx, name in enumerate(cow): #cow에서 문자(A, B, C, ...)와 문자의 위치
    cow_index[name].append(idx)
"""
cow_index = {
  'A': [0,2],
  'B': [1,4],
  'C': [3,5],
  ...
}
"""

cnt = 0

# 소 이름만 있는 리스트
cow_names = list(cow_index.keys())

for i in range(26):
    a1, a2 = cow_index[cow_names[i]] #cow_names i번째 소의 각 위치(a1, a2)
    for j in range(i+1, 26):
        b1, b2 = cow_index[cow_names[j]] #cow_names j번째 소의 각 위치(b1, b2)
        
        # a1 < b1 < a2 < b2 같은 식일 때 교차가 발생
        if (a1 < b1 < a2 < b2) or (b1 < a1 < b2 < a2):
            cnt += 1

print(cnt)