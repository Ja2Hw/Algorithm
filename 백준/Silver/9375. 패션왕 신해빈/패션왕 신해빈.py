import sys

T = int(sys.stdin.readline()) #테스트 케이스 수

for _ in range(T):
    wears = {}
    n = int(sys.stdin.readline()) #의상 수
    for _ in range(n): # 의상 개수만큼 반복
        name, kind = sys.stdin.readline().strip().split()
        if kind in wears: #이미 있는 종류면
            wears[kind].append(name) #딕셔너리에 의상 이름만 추가함
        else:
            wears[kind] = [name] #없으면 딕셔너리에 추가
            
    cnt = 1
    
    for x in wears:
        cnt *= (len(wears[x]) + 1) #해당 종류에서 아무것도 고르지 않는 경우도 포함해 +1
        
    print(cnt-1) #아무것도 안 입게 된 경우 제외