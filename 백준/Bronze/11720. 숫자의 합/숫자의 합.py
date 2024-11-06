import sys

n = int(sys.stdin.readline())

s = sys.stdin.readline().strip()
su = 0

for i in range(n):
    su += int(s[i])

print(su)