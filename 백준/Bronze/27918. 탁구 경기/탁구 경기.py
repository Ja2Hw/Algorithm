import sys

n = int(sys.stdin.readline())
x = 0
y = 0

for _ in range(n):
    win = sys.stdin.readline().strip()
    if win == 'D':
        x += 1
    else:
        y += 1
    if abs(x-y) >= 2:
        break
        
print(f"{x}:{y}")