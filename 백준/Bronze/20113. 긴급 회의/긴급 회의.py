import sys
from collections import Counter

n = int(sys.stdin.readline())
vote = list(map(int, sys.stdin.readline().split()))
# vote만 사용하면 0 값 처리가 어려움
# 0을 제외한 후보들의 투표 수를 카운트
counter = Counter(vote)
if 0 in counter:
    del counter[0]

# 투표 수가 비어있으면 "skipped"
if not counter:
    print("skipped")
else:
    # 최다 득표수와 해당 득표수의 후보자 수 확인
    max_vote = max(counter.values())
    #res = [i for i, value in enumerate(vote) if value == max_vote]
    res = [i for i, value in counter.items() if value == max_vote]
    
    if len(res) > 1:
        print("skipped")
    else:
        print(res[0])