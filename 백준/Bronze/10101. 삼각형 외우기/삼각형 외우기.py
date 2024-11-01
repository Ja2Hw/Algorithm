import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())

if a==b and b==c and a==60:
    print("Equilateral")
elif a+b+c == 180:
    if a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
    