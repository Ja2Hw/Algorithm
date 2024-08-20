import sys

N = int(sys.stdin.readline())

stk = [] # 메인 스택
result = [] # 결과 +- 들어감
stop = False

tmp = 1 #시작하는 수

for _ in range(N):
    num = int(sys.stdin.readline())
    while tmp <= num: # 찾고 있던 숫자 나오기 전까지 push (+)
        stk.append(tmp)
        result.append('+')
        tmp += 1
    if stk[-1] == num: # 메인 스택 마지막(마지막에 넣은 tmp)이 num일 때 = 찾고 있던 숫자일 때
        stk.pop()
        result.append('-')
    else:
        stop = True
        
if stop:
    print("NO")
else:
    for r in result:
        print(r)
    