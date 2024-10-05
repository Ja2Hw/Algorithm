"""
fi(n)의 0 개수 = fi(n-1)의 0 개수 + fi(n-2)의 0 개수

"""
import sys
T = int(sys.stdin.readline()) # 테스트 케이스의 수

dp = [-1] * 41
zero = [0] * 41
one = [0] * 41

dp[0] = 0
dp[1] = 1

zero[0] = 1
one[1] = 1

def fibo(n):
    if dp[n] != -1:
        return

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
        zero[i] = zero[i - 2] + zero[i - 1]
        one[i] = one[i - 2] + one[i - 1]

for i in range(T):
    n = int(input())
    fibo(n)
    print(zero[n], one[n])
    
"""
T = int(input())
for _ in range(T):
    N = int(input())
    a, b = 1, 0 # 0과 1이 호출된 횟수
    for i in range(N):
        # 0은 1이 호출된 횟수만큼, 1은 0과 1이 호출된 합만큼 출력됨
        a,b = b, a+b 
    print(a,b)
출처: https://edder773.tistory.com/64 [개발하는 차리의 학습 일기:티스토리]
"""