class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        revers = str(x)[::-1]
        return revers == str(x)