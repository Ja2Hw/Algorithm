import sys

L, R, A = map(int, sys.stdin.readline().split())

while A > 0 : # 양발잡이 나눠 가지기
    if L == R: #숫자가 같을 때
        if A % 2 == 0: # 총인원 짝수일 때
            res = L + R + A
        else: # 총인원 홀수일 때
            res = L + R + A - 1
        break
    elif L > R: # 왼발잡이가 더 많을 때
        R += 1
        A -= 1
    else: #오른발잡이가 더 많을 때
        L += 1
        A -= 1
    
else:
    res = min(L, R) * 2

print(res)