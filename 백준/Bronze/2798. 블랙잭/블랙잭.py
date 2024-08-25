import sys
# N = 카드 수, 3장의 합이 M과 최대한 가까워지게
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
res = 0
for a in range(N): #처음부터 N까지
    for b in range(a+1, N): #a다음부터 N까지
        for c in range(b+1, N): #b 다음부터 N까지
            if cards[a] + cards[b] + cards[c] > M:
                continue
            else:
                res = max(res, cards[a] + cards[b] + cards[c])   
print(res)            