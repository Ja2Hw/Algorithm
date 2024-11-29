import sys

jh = sys.stdin.readline().strip()
doc = sys.stdin.readline().strip()

print('go') if len(jh)>=len(doc) else print('no')