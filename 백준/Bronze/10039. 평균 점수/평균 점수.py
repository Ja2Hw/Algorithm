import sys
input = sys.stdin.readline

score = [max(int(input()), 40) for _ in range(5)]

print(sum(score)//len(score))