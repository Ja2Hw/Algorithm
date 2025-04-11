import sys

n = int(sys.stdin.readline())
call = list(map(int, sys.stdin.readline().split()))

y = 0
m = 0

for i in call:
    # 영식 요금제
    y += ((i//30)+1)*10
        
    # 민식 요금제
    m += ((i//60)+1)*15
        
if y < m:
    print('Y', y)
elif y > m:
    print('M', m)
else:
    print('Y M', y)
    
