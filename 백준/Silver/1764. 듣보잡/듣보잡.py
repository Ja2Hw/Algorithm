# 듣보잡
import sys
N, M = map(int, sys.stdin.readline().split())
res = []
Never_listen = set() #set은 in으로 탐색할 때 해시테이블을 사용해서 시간복잡도가 O(1)임

for _ in range(N):
    Never_listen.add(sys.stdin.readline().rstrip())
    
for _ in range(M):
    Never_watch = sys.stdin.readline().rstrip()
    if Never_watch in Never_listen:
        res.append(Never_watch)

print(len(res))
for i in sorted(res):
    print(i)
    
"""
시간 초과
import sys
N, M = map(int, sys.stdin.readline().split())
res = []
Never_listen = [sys.stdin.readline().rstrip() for _ in range(N)]
for _ in range(M):
    Never_watch = sys.stdin.readline().rstrip()
    if Never_watch in Never_listen:
        res.append(No_watch)
        
print(len(res))
for r in sorted(res):
    print(r)


"""