# 31824 근로장학생
# 실버 3

import sys

input = sys.stdin.readline

# 정보 n개, 질문 m개
N, M = map(int, input().split())

# (Q_i, A_i) : (영단어, 뜻)
words = [tuple(input().split()) for _ in range(N)]

# 질문
que = [input().strip() for _ in range(M)]

for S in que:
    result = [] # 결과 버퍼, A_i들을 이어붙임
    L = len(S) # 문장 길이
    
    # 문장의 각 위치 k를 0..L-1 순서로 탐색
    for k in range(L):
        matches = [] # 위치 k에서 일치한 (Q_i, A_i) 모음
        
        # 모든 (Q_i, A_i)에 대해 현재 위치 k에서 시작해 정확히 일치하는 (Q_i, A_i) 수집
        for q, a in words:
            # k부터 len(q) 만큼 잘라서 q와 일치하는지 확인
            if k + len(q) <= L and S.startswith(q, k):
                matches.append((q, a))
        
        # 사전순 Q_i 기준으로 정렬 후 A_i 를 버퍼에 추가
        if matches:
            matches.sort(key=lambda x: x[0]) # Q_i 기준 사전순
            result.extend(a for _, a in matches)
    
    
    if result: # 최소 하나라도 매칭됐으면
        print(''.join(result)) # A_i 들을 순서대로 이어붙여 출력
    else: # 아무것도 못 찾은 경우
        print(-1)
