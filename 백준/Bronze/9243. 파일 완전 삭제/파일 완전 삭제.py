import sys

n = int(sys.stdin.readline())
before = sys.stdin.readline().strip()
after = sys.stdin.readline().strip()

if n%2==0:
    if before == after:
        print("Deletion succeeded")
    else:
        print("Deletion failed")
else:
    for i in range(len(before)):
        if before[i]==after[i]:
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")
