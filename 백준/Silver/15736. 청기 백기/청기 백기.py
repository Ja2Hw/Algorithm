# 15736 청기 백기
# 실버 4

import sys, math
input = sys.stdin.readline

# 출전한 학생 수이자 깃발 수
N = int(input())

# 최종적으로 백색인 깃발은 약수의 개수가 홀수인 번호 뿐임
# 약수가 홀수 개인 경우는 완전제곱수 뿐!
print(math.isqrt(N))   # ⌊√N⌋를 정수로 바로 돌려줌


""" 메모리 초과 (브루트포스)

# 초기 깃발은 청색=0 / 백색=1
flags = [0]*N

# i번째 학생
for i in range(1, N+1):
    # i의 배수의 깃발 뒤집기
    tmp = i
    while tmp < N:
        if flags[tmp] == 0:
            flags[tmp] = 1
        else:
            flags[tmp] = 0
        tmp += i

# N번째 학생까지 진행 후 백색 깃발 수
print(flags.count(1))

"""