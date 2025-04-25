# 29735 택배가 안와잉

import sys

input = sys.stdin.readline

def parse_time(hhmm):
    h, m = map(int, hhmm.split(':'))
    return h * 60 + m

def format_time(minutes):
    minutes %= 1440
    return f"{minutes // 60:02d}:{minutes % 60:02d}"

# 입력
S, E = input().split()
N, T = map(int, input().split())

start = parse_time(S)
end = parse_time(E)

current_time = start
days = 0
remaining = N

while remaining > 0:
    # 이번 배달 끝나는 시간
    finish_time = current_time + T

    # 수정 포인트: 배송 끝나는 시간이 퇴근 시간 "이상"이면 오늘 퇴근
    if finish_time >= end:
        days += 1
        current_time = start
    else:
        current_time = finish_time
        remaining -= 1

# 브실이의 택배는 마지막으로 하나 더 배송해야 함
finish_time = current_time + T
if finish_time >= end:  # 여기서도 마찬가지
    days += 1
    current_time = start + T
else:
    current_time = finish_time

print(days)
print(format_time(current_time))
