import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    num1 = sys.stdin.readline().strip()
    num2 = ''.join(reversed(num1))
    res = str(int(num1)+int(num2))
    
    print("YES" if res == res[::-1] else "NO")
