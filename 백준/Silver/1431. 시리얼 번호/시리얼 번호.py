import sys

n = int(sys.stdin.readline().strip())
serial = []

for _ in range(n):
    s = sys.stdin.readline().strip()
    
    num = 0
    for i in s: # 숫자만 더하기
        if i.isdigit():
            num += int(i)
    serial.append((s, num)) # 문자열, 숫자 합 같이 묶어서 저장하기

serial.sort(key=lambda x: (len(x[0]), x[1], x[0])) # 길이, 숫자, 사전순으로 정렬

#print('---')

for s, _ in serial:
    print(s)