import sys

N, M = map(int, sys.stdin.readline().split())

Pokedex = {} #딕셔너리

for i in range(1, N+1): #도감 입력 받기
    pokemon = sys.stdin.readline().rstrip()
    Pokedex[i] = pokemon
    Pokedex[pokemon] = i

for i in range(M): #문제 풀기
    Quiz = sys.stdin.readline().rstrip()
    if Quiz.isdigit(): #정수로 바꿀 수 있는 문자열일 때 = 숫자로 된 문자열일 때
        print(Pokedex[int(Quiz)])
    else:
        print(Pokedex[Quiz])

"""
#시간 초과
import sys
N, M = map(int, sys.stdin.readline().split())
Pokedex = [sys.stdin.readline().rstrip() for _ in range(N)]
Quiz = [sys.stdin.readline().rstrip() for _ in range(M)]

for q in Quiz:
    if q.isdigit(): #숫자 받아서 이름 출력
        print(Pokedex[int(q)-1])
    else: #이름 받아서 숫자 출력
        print(Pokedex.index(q)+1)

"""