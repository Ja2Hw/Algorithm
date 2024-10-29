import sys
#달팽이는 낮에 A미터 올라가고 밤에 B미터 미끄러짐. V미터인 나무 막대를 올라감
#V-B 까지만 도달하면 V까지 도달한 것이나 같음
#(V-B)를 (A-B)로 나눈 몫 = 달팽이가 올라가는 일 수
#딱 안 떨어지면 하루 더 가면 되니까 +1

A, B, V = map(int, sys.stdin.readline().split())

if (V-B) % (A-B) == 0:
    print((V-B)//(A-B))
else:
    print((V-B)//(A-B) + 1)


"""
시간 초과
day = 1

while (day*(A-B)) < (V-A):
    day += 1

print(day+1)
"""