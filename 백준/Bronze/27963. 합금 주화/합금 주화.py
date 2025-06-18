# 27963 합금 주화
# 브론즈 1

import sys
input = sys.stdin.readline

# d1, d2 = 기념주화를 이루는 두 가지 금속의 밀도
# x = 두 가지 금속 중 밀도가 더 높은 쪽이 기념주화에서 차지하는 질량의 비율(%)
d1, d2, x = map(int, input().split())

# 밀도 높은 것 낮은 것 구분
d_h = max(d1, d2)
d_l = min(d1, d2)

# 질량 비율 구분
m_h = x
m_l = 100 - x

# 전체 밀도 계산
result = (m_h + m_l) / (m_h / d_h + m_l / d_l)

# 출력 (절대/상대 오차 1e-6 허용)
print(result)