import sys

b = []
c = []

for _ in range(3):
    k = int(sys.stdin.readline())
    b.append(k)
    
for _ in range(2):
    k = int(sys.stdin.readline())
    c.append(k)

print(min(c)+min(b)-50)