import sys

S = sys.stdin.readline().rstrip()

zero = 0
one = 0
tmp = 'start' #바로 앞에 있는 숫자
for i in S:
    if tmp == 'start':
        tmp = i
    #elif tmp == i: #앞에 거랑 숫자가 같을 때    
    
    if tmp != i: #앞이랑 숫자가 다를 때
        if tmp == '0': #0이 끝났을 때
            zero += 1
        else: #1이 끝났을 때
            one += 1
        tmp = i

if tmp == '0':
    zero += 1
else:
    one += 1
        
print(min(zero, one))