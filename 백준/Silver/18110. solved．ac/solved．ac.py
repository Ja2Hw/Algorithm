import sys

def newRound(num):
    if ( num - int(num) ) < 0.5:
        return int(num)
    return int(num) + 1


n = int(sys.stdin.readline().rstrip())
    
if n == 0:
    print(0)

else:
    d = []
    for _ in range(n):
        d.append(int(sys.stdin.readline().rstrip()))
        
    d.sort()
    idx = newRound(n * 0.15)
    
    print(newRound(sum(d[idx:n-idx])/len(d[idx:n-idx])))