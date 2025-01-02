import sys


n = int(sys.stdin.readline())
top = list(map(int, sys.stdin.readline().split()))
cnt = 0
recent = -1
for t in top:
    if recent == -1:
        recent = t
        cnt += 1
    elif recent <= t: # 넘어간 탑이 뒤 타워보다 낮거나 같을 때
        cnt += 1
        recent = t
    else: # 높을 때
        recent = t

print(cnt)