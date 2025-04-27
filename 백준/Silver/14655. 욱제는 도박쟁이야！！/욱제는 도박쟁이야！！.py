# 14655 욱제는 도박쟁이야
# 실버 5

import sys
input = sys.stdin.readline

n = int(input())

one_coin = list(map(int, input().split()))
two_coin = list(map(int, input().split()))

print(sum(abs(x) for x in one_coin) + sum(abs(x) for x in two_coin))
# 동전을 3개씩 뒤집는다, 양 끝의 동전만 뒤집는 게 가능하다... 이런 조건은 사실 함정이라 볼 수 있다
# 동전을 뒤집는 횟수에 제한이 없기 때문에, 항상 최적의 값을 내는 게 가능한 것이다
# 절댓값 기준 최고치로 만들어 계산하면 된다.