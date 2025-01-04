import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    base = a%10
    
    #시간 초과
    #print((a**b)%10)
    
    # 일의 자리만 쓰니까 0~9를 승수 처리해서 일의 자리만 보면 그만임
    if base==0:#1의 자리가 0인 경우(10의 배수)
        print(10)
    elif base==1 or base==5 or base==6:#1,5,6인경우
        print(base)
    elif base==4 or base==9:#4,9 : 값을 그대로 가지거나, 제곱의 나머지
        if b%2==0:
            print((base**2)%10)
        else:
            print(base)
    else:#2,3,7,8
        if b%4==0:
            print(base**4%10)#4로 나눈 나머지를 바로 쓰면 오류 남
        else:
            print(base**(b%4)%10)   