import sys

r = 31
M = 1234567891
L = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()
res = 0

# 아스키코드에 96빼면 알파벳 숫자임
# a의 아스키 코드 = 97
# ord(x) => 문자를 아스키코드 혹은 유니코드로 변환
# chr(x) => 아스키코드를 문자로 변환
for i in range(L):
    res += (ord(string[i]) - 96)*(r**i)
print(res%M)
