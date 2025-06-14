# 2033 반올림
# 브론즈 1

import sys
input = sys.stdin.readline

N = input().strip()
N_list = list(N)

if len(N_list) > 1:
    # 마지막 자리(일의 자리)부터 두 번째 자리까지 순회하며 반올림 처리
    for i in range(len(N_list) - 1, 0, -1):
        # 현재 자리 숫자가 5 이상이면 앞자리를 1 올림
        if int(N_list[i]) >= 5:
            N_list[i-1] = str(int(N_list[i-1]) + 1)
        # 반올림된 후든 아니든, 현재 자리 숫자는 0으로 고정
        N_list[i] = '0'
    # 맨 앞자리가 '10'이 된 경우도 int 변환으로 자동 처리됩니다
    result = int(''.join(N_list))
    print(result)
else:
    # 한 자리 수면 그대로 출력
    print(int(N_list[0]))