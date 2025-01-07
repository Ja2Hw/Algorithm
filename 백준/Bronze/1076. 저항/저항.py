import sys

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

a = str(color.index(sys.stdin.readline().strip()))
b = str(color.index(sys.stdin.readline().strip()))
c = str(10**color.index(sys.stdin.readline().strip()))

print(int(a+b+c[1:]))