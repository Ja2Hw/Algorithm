import sys

n = sys.stdin.readline().strip()
mobis = 'MOBIS'
fine = True

for m in mobis:
    if m in n:
        fine = True
        continue
    else:
        fine = False
        break
if fine:
    print("YES")
else:
    print("NO")