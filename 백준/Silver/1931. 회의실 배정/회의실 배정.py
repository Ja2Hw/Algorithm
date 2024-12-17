import sys

# N개의 회의
n = int(sys.stdin.readline())
times = []
cnt = 0 # 숫자 세기

for _ in range(n):
    times.append(list(map(int, sys.stdin.readline().split())))

times.sort(key=lambda x: (x[1], x[0])) # 빨리 끝나는 순서대로 정렬
#print(times)

now = 0 # 끝났을 때의 시간 기록

for start, end in times:
    if now <= start: # 빨리 끝나는 순서에서, 다음 회의 시간이 현재 회의 종료된 시간과 같거나 늦을 때
        cnt += 1
        now = end

print(cnt)
