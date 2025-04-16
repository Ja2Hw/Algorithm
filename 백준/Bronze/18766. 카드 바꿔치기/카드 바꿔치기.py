# 18766 카드 바꿔치기

import sys

# 테스트케이스 수 t 
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline()) # 카드의 개수
    one = sorted(list(sys.stdin.readline().split()))
    two = sorted(list(sys.stdin.readline().split()))
    
    # if one == two:
    #     print("NOT CHEATER")
    # else:
    #     print("CHEATER")
    
    for t in two:
        if t not in one:
            print("CHEATER")
            break
        else:
            if one.count(t) == two.count(t):
                continue
            else:
                print("CHEATER")
                break
    else:
        print("NOT CHEATER")