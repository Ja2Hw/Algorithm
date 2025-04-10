import sys

n = int(sys.stdin.readline())

cnt = 0

for i in range(1, n+1):
    s = str(i)
    
    cnt += s.count('3')
    cnt += s.count('6')
    cnt += s.count('9')
    
print(cnt)