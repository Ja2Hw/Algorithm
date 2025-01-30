# 15702 중간고사 채점
# 실버 5

import sys

# 문제의 개수 n, 응시자의 수 m
n, m = map(int, sys.stdin.readline().split())

scores = list(map(int, sys.stdin.readline().split()))

student_scores = {}

for _ in range(m):
    data = sys.stdin.readline().split()
    id = int(data[0])
    res = data[1:]
    
    # 총점 계산
    total_score = 0
    for i in range(n):
        if res[i] == 'O':
            total_score += scores[i]
    
    # 학생의 수험번호와 총점 저장
    student_scores[id] = total_score
    
# 최고 점수를 받은 학생 찾기
max_score = max(student_scores.values())
best_students = [id for id in student_scores.keys() if student_scores[id] == max_score]

# 동점자가 있는 경우 가장 작은 수험번호 선택
best_student = min(best_students)

# 결과 출력
print(best_student, max_score)