# 25204 문자열 정렬
# 실버 4

import sys
import functools

def compare(s1, s2):
    # 두 문자열을 한 글자씩 비교
    i = 0
    min_len = min(len(s1), len(s2))
    
    while i < min_len:
        # 문자가 같으면 다음 문자로
        if s1[i] == s2[i]:
            i += 1
            continue
            
        # 다른 문자를 발견했을 때
        # 1. 붙임표 우선순위 처리
        if s1[i] == '-':
            return 1  # s2가 앞선다
        if s2[i] == '-':
            return -1  # s1이 앞선다
            
        # 2. 알파벳 비교
        if s1[i].lower() != s2[i].lower():
            # 대소문자 무시했을 때 다른 알파벳이면 알파벳 순서
            return -1 if s1[i].lower() < s2[i].lower() else 1
        else:
            # 같은 알파벳이지만 대소문자가 다른 경우 대문자가 앞선다
            return -1 if s1[i].isupper() and s2[i].islower() else 1 if s1[i].islower() and s2[i].isupper() else 0
    
    # 여기까지 왔다면 접두사 관계 확인
    if len(s1) == len(s2):
        return 0
    # 짧은 문자열이 긴 문자열의 접두사면 짧은 것이 앞선다
    return -1 if len(s1) < len(s2) else 1

# 입력 처리
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    strings = [input().strip() for _ in range(N)]
    
    # functools.cmp_to_key를 사용하여 정렬
    sorted_strings = sorted(strings, key=functools.cmp_to_key(compare))
    
    # 순차적으로 출력
    for s in sorted_strings:
        print(s)