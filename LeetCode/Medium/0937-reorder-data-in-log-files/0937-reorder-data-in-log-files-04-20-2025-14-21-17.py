"""
# 로그 파일 재정렬 : 람다와 + 연산자를 이용

로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다
4. 숫자 로그는 입력 순서대로 한다
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []

        for log in logs: # 숫자 로그인지 문자 로그인지 확인
            if log.split()[1].isdigit(): # 식별자 뒤에 로그가 숫자라면
                digits.append(log)
            else: # 식별자 뒤에 로그가 문자라면
                letters.append(log) 

        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

        