import sys
input = sys.stdin.readline

v = int(input())
vote = input().strip()

if vote.count('A') > vote.count('B'):
    print('A')
elif vote.count('A') < vote.count('B'):
    print('B')
else:
    print('Tie')