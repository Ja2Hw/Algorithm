# 28682 브론즈1
# 재우야 임관하자

import sys

# 평행세계의 개수 n
n = int(sys.stdin.readline())

# 첫번째 선택 : 순서대로 입력 받기
sb = ['swimming', 'bowling', 'soccer']
first = [sb[i%3] for i in range(n)]

# 첫번째 선택 출력
print(' '.join(first)+'\n')
sys.stdout.flush()

# 교수님이 대답
prof = sys.stdin.readline().strip().split()

# 최종 선택
res = []
for i in range(n):
    now = first[i]
    prof_say = prof[i]
    
    # 가능한 선택지
    all_sb = {'swimming', 'bowling', 'soccer'}
    remain_sb = all_sb - {now, prof_say}
    
    # 남은 과목 하나 뿐임
    res.append(remain_sb.pop())
    
print(' '.join(res)+'\n')
sys.stdout.flush()
    