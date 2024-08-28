import sys

while True:
    N = str(sys.stdin.readline().rstrip())
    wrong = False
    if int(N) == 0:
        break
    else:
        for i in range(0, len(N)//2+1):
            if N[i] != N[-(i+1)]:
                print("no")
                wrong = True
                break
        if wrong == False:
            print("yes")