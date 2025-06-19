# 24039 2021은 무엇이 특별할까?
# 실버 5

import sys
input = sys.stdin.readline

n = int(input())

primes = [] # 소수 리스트

for num in range(2, 151): # N의 값이 10000 이하이므로 적당한 수까지만 확인해도 됨
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: # 약수를 발견하면 break
            break
    else: # 약수 발견 못하면 소수 리스트에 추가
        primes.append(num)

# 연속된 소수의 곱 조회
i = 0
while n >= (primes[i]*primes[i+1]):
    i += 1

print(primes[i]*primes[i+1])