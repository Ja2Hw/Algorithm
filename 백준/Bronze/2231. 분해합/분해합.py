import sys

N = int(sys.stdin.readline())

res = 0
end = False

while res < N:
    tmp = 0
    for r in str(res):
        tmp += int(r)
    tmp += res
    if tmp == N:
        end = True
        print(res)
        break
    res += 1
if end == False:
    print(0)
