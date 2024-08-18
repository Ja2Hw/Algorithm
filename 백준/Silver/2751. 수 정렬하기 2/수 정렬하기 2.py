import sys

N = int(sys.stdin.readline())
input_list = sorted([int(sys.stdin.readline()) for _ in range(N)])
for i in input_list:
    print(i)