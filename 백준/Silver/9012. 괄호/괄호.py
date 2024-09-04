#괄호
import sys

T = int(sys.stdin.readline())
PS = [str(input()) for _ in range(T)]

for p in PS:
    op = 0 # '(' 개수
    for i in p:
        if i == '(':
            op += 1
        else:
            op -= 1
        if op < 0:
                print("NO")
                break
    if op == 0:
        print("YES")
    elif op > 0:
        print("NO")
        
