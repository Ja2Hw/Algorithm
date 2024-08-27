import sys

N = int(sys.stdin.readline())

tmp = 1
i = 1
while True:
    if N == 1:
        print(1)
        break
    elif N <= (tmp + (6*i)):
        print(i+1)
        break
    else:
        tmp += (6*i)
    i += 1

'''
1 + 6 + 12 + 18
1   2    3    4
1
2 ~ 7
8 ~ 19
20 ~ 37
'''    