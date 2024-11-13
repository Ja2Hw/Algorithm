# 2xn 직사각형을 2x1, 1x2 블럭으로 채우기
# 방법의 수를 10007로 나눈 나머지 출력
import sys
n = int(sys.stdin.readline())

res  = [0]*1001
res[1] = 1
res[2] = 2

for i in range(3, 1001):
    res[i] = (res[i-1]+res[i-2])%10007

print(res[n])

"""
1=> 1
2=> 2
3=> 3
4=> 5
5=> 8
6=> 13

n=> (n-1)+(n-2)
"""