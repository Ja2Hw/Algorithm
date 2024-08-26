import sys

N = int(sys.stdin.readline())
'''
if (N % 5) % 3 == 0:
    print((N//5) + ((N % 5)//3))
elif (N % 3) == 0:
    print(N//3)
else:
    print(-1)
'''
cnt = N
five = 0
while five * 5 <= N :
    if (N - (5*five)) % 3 == 0:
        cnt = min(cnt, five + ((N - (5*five)) // 3))
        #print(cnt)
    five += 1
if cnt == N:
    print(-1)
else:
    print(cnt)  