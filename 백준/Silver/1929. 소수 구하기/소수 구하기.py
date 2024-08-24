# 에라토스테네스의 체
import sys

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    if i==1:
        continue
    for j in range(2, int(i**0.5)+1): #루트 i
        if i % j == 0:
            break 
    else:
        print(i)
        
"""
def isPrime(a):
    if(a==1):
        return False
    for i in range(2, a):
        if(a%i==0):
            return False
    return True

for num in range(M, N+1):
    if isPrime(num) == True:
        print(num)
"""