import sys

N = int(sys.stdin.readline())
input_list = [int(sys.stdin.readline()) for _ in range(N)]
for i in sorted(input_list):
    print(i)