# 27494 2023년은 검은 토끼의 해
# 브론즈 1

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

# 2023을 부분수열로 포함하는지 확인
def check(s: str) -> bool:
    target = '2023'
    ti = 0 # 한자리 맞출 때마다 표시, 4면 2023 다 찾은 거
    for ch in s: # 문자열 한자리씩 봄
        if ch == target[ti]:
            ti += 1
            if ti == 4: #
                return True
    return False

for number in range(1, N+1):
    s = str(number)
    if len(s) < 4: # 네자릿수 미만이면 성립 불가능으로 스킵
        continue
    if check(s):
        cnt += 1
print(cnt)


"""
# 20023 같은 것도 정답 복권이 될 수 있음을 간과한 코드

remove_set = {'1', '4', '5', '6', '7', '8', '9'}

for number in range(1, N+1):
    num = list(str(number))
    num = [i for i in num if i not in remove_set]
    
    check = ''.join(num)
    if '2023' in check:
        cnt += 1

print(cnt)

"""
