# 27951 옷걸이
# 브론즈 1

import sys

n = int(sys.stdin.readline())  # 옷걸이의 개수
a = list(map(int, sys.stdin.readline().split()))  # 옷걸이의 종류
u, d = map(int, sys.stdin.readline().split())  # 상의 개수 u, 하의 개수 d

# 상의와 하의를 걸 수 있는 옷걸이의 수를 계산
upper_hangers = a.count(1) + a.count(3)
lower_hangers = a.count(2) + a.count(3)


# 상의와 하의를 모두 걸 수 있는지 확인
if upper_hangers >= u and lower_hangers >= d:
    print("YES")
    result = []
    for hanger in a:
        if hanger == 1:
            if u > 0:
                result.append('U')
                u -= 1
            else:
                result.append('D')
                d -= 1
        elif hanger == 2:
            if d > 0:
                result.append('D')
                d -= 1
            else:
                result.append('U')
                u -= 1
        else:  # hanger == 3
            if u > 0:
                result.append('U')
                u -= 1
            else:
                result.append('D')
                d -= 1
    print("".join(result))
else:
    print("NO")