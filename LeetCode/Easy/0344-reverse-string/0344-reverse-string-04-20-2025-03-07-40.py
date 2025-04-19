# 문자열 뒤집기 : 투 포인터를 이용한 스왑

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) -1 #인덱스 기준이니까 -1 해줌
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
