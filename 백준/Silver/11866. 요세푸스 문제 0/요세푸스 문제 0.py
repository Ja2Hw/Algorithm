import sys

n, k = map(int, sys.stdin.readline().split())

idx = 0
og = [i for i in range(1, n+1)]
result = []
while og:
    idx += k-1
    if idx >= len(og):
        idx %= len(og)
    result.append(str(og.pop(idx)))
        
print("<", ", ".join(result), ">", sep="")