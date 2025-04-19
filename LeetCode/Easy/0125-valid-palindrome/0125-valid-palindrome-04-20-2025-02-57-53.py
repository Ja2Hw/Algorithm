class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:

            # xx.isalnum() = 영문자, 숫자 여부 판별 함수
            if char.isalnum():
                strs.append(char.lower())
        
        # 펠린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True