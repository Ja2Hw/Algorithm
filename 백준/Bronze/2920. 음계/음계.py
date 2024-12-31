import sys

hi = list(map(int, sys.stdin.readline().split()))

if hi == sorted(hi):
    print("ascending")
elif hi == sorted(hi, reverse=True):
    print("descending")
else:
    print("mixed")
    