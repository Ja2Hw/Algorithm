# 20546 기적의 매매법
# 실버 5

import sys

money = int(sys.stdin.readline().strip())
stocks = list(map(int, sys.stdin.readline().split()))

# 준현이 전략
jh = money
jh_cnt = 0
for i in range(len(stocks)):
    if jh >= stocks[i]:
        jh_cnt += jh // stocks[i]  # 살 수 있는 만큼 주식 매수
        jh %= stocks[i]  # 남은 돈 갱신

# 성민이 전략
sm = money
sm_cnt = 0
up_count = 0
down_count = 0

for i in range(1, len(stocks)):
    if stocks[i-1] < stocks[i]:
        up_count += 1
        down_count = 0
    elif stocks[i-1] > stocks[i]:
        down_count += 1
        up_count = 0
    else:
        up_count = 0
        down_count = 0

    # 3일 연속 상승 시 매도
    if up_count >= 3:
        if sm_cnt > 0:
            sm += sm_cnt * stocks[i]
            sm_cnt = 0
    
    # 3일 연속 하락 시 매수
    if down_count >= 3:
        if sm >= stocks[i]:
            sm_cnt += sm // stocks[i]
            sm %= stocks[i]

# 최종 수익 비교
jh_total = jh + jh_cnt * stocks[-1]
sm_total = sm + sm_cnt * stocks[-1]

if jh_total > sm_total:
    print("BNP")
elif jh_total < sm_total:
    print("TIMING")
else:
    print("SAMESAME")