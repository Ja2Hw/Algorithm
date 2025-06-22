# 31495 그게 무슨 코드니
# 브론즈 4

import sys
input = sys.stdin.readline

S = input().strip()

if S[0] =='"' and S[-1] == '"':
    if len(S)==2 or len(S)==1:
        print("CE")
    else:
        print(S[1:len(S)-1])
else:
    print("CE")