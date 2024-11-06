import sys

st = [sys.stdin.readline().strip() for _ in range(3)]

for i in range(2, -1, -1):
    x = sys.stdin.readline().strip()
    if st[i].isdigit():
        res = int(st[i]) + (3-i)
        break
        
if res % 15 == 0:
    print("FizzBuzz")
elif res % 3 == 0:
    print("Fizz")
elif res % 5 == 0:
    print("Buzz")
else:
    print(res)
    