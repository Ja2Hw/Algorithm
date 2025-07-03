import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
virus_computer = [False] * (N + 1)
result = N

for _ in range(Q):
    query = input().split()
    if len(query) > 1:
        case, x = int(query[0]), int(query[1])
    else:
        case = int(query[0])

    if case == 1:
        if not virus_computer[x]:
            result -= 1
        virus_computer[x] = True

    elif case == 2:
        if virus_computer[x]:
            result += 1
        virus_computer[x] = False

    elif case == 3:
        print(result)
