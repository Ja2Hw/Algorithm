import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for _ in range(m):
    k = int(input())
    stack = list(map(int, input().split()))
    # 위에서부터 아래로 검사 (책 쌓인 순서대로)
    for i in range(k - 1):
        if stack[i] < stack[i + 1]:
            print("No")
            exit()

print("Yes")