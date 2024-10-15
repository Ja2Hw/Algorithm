import sys

t = int(sys.stdin.readline()) #테스트케이스의 수

wave = [1, 1, 1, 2, 2]
for i in range(5, 101):
    wave.append(wave[i-1]+wave[i-5])
    
for _ in range(t):
    n = int(sys.stdin.readline())
    print(wave[n-1])
