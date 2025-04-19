class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs : Deque = collections.deque()

        for char in s:
            # x.isalnum() = 영문자, 숫자 여부 판별 함수
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            # strs의 첫번째와 마지막 요소가 같지 않으면
            if strs.popleft() != strs.pop():
                return False
        
        return True
