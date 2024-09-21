import sys

#저장된 전체 사이트 수 N개, 비밀번호를 찾으려는 사이트의 수 M개
N, M = map(int, sys.stdin.readline().split())

acc = {} #딕셔너리

for _ in range(N):
    site, pw = map(str, sys.stdin.readline().strip().split())
    acc[site] = pw

for _ in range(M):
    site = sys.stdin.readline().strip()
    print(acc[site])



"""
시간 초과
all_acc = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
#select = [sys.stdin.readline().strip() for _ in range(M)]

for _ in range(M):
    sel = sys.stdin.readline().rstrip()
    for a in all_acc:
        if a[0] == sel:
            print(a[1])
            break

"""