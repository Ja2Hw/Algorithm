import sys

X = int(sys.stdin.readline())

sticks = [64, 32, 16, 8, 4, 2, 1]

cnt = 0

for i in range(len(sticks)):
  if X == 0:
    break
  if sticks[i] <= X:
    X -= sticks[i]
    cnt += 1

print(cnt)