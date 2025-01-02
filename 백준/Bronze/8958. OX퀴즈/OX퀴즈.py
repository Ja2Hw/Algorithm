import sys

t = int(sys.stdin.readline())

for _ in range(t):
    quiz = sys.stdin.readline().strip()
    score = 0
    tmp_score = 0
    for q in quiz:
        if q == 'O':
            tmp_score += 1
            score += tmp_score                
        else:
            tmp_score = 0

    print(score)