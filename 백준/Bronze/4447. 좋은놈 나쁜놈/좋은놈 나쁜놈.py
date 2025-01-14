import sys

n = int(sys.stdin.readline())

heros = [sys.stdin.readline().strip() for _ in range(n)]

for hero in heros:
    g = hero.count('g') + hero.count('G')
    b = hero.count('b') + hero.count('B')

    if g > b:
        print(f'{hero} is GOOD')
    elif g < b:
        print(f'{hero} is A BADDY')
    else:
        print(f'{hero} is NEUTRAL')