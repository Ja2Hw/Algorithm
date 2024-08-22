import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
cnt = 0

for n in nums:
  for i in range(2, n+1):
    if n % i == 0:
      if n == i:
        cnt += 1
      
      break

print(cnt)