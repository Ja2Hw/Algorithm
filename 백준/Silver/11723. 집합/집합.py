import sys

S = set()

M = int(sys.stdin.readline())

for _ in range(M):
    cal = sys.stdin.readline().strip().split()
    
    if len(cal) == 1:
        if cal[0] == "all":
            S = set(list(range(1, 21)))
        elif cal[0] == "empty":
            S = set()
    else:
        kind, x = cal[0], cal[1]
        x = int(x)
    
        if kind == "add" and x not in S:
            S.add(x) #set은 add
        elif kind == "remove" and x in S:
            #S.discard(x) -> 이걸로 하면 조건 달지 않아도 x 없으면 무시함
            S.remove(x)
        elif kind == "check":
            print(1 if x in S else 0)
        elif kind == "toggle":
            if x in S: #S 안에 x가 있으면 삭제
                S.discard(x)
            else: # 없으면 추가
                S.add(x)