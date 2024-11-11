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
    # for와 같은 레벨에 있는 else문은 반복문 else이다.
    # for문이 중간에 break로 중단되지 않고 끝까지 모든 반복이 실행된 경우에만 else 블록이 실행된다!
    else: 
        print("Deletion succeeded")
