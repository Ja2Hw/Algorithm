import sys

# n개의 줄에 m개의 정수로 땅 높이 주어짐
# b는 인벤토리에 있는 블록의 개수
# (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타냄
# 땅의 높이는 256보다 작거나 같은 자연수 또는 0
# 1번 작업 : 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
# 2번 작업 : 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
# 1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다
# 출력 : 땅을 고르는 데에 걸리는 시간과 땅의 높이
n, m, b = map(int, sys.stdin.readline().split())

# 높이 데이터 입력
gr = []
for _ in range(n):
    gr.extend(map(int, sys.stdin.readline().split()))

time = [0 for i in range(257)] # time[k]에 땅높이가 k일때의 소요시간 저장
height = 0
for g in range(257):
    block = b # 인벤토리에 남은 블록 수
    for i in gr:
        if i <= g: # i == g이면 g-i=0
            time[g] += g - i
            block -= g - i
        else:
            time[g] += 2 * (i - g)
            block += i - g
    if block >= 0 and time[g] <= time[height]: # 오름차순으로 순회하므로, 답이 여러 개 있을 때 그중에서 땅의 높이가 가장 높은 것을 저장하게 됨
        height = g # 최소 소요 시간인 땅높이 저장

print(time[height], height)