class Solution:
    def longestPalindrome(self, s: str) -> str:
        best ="";next=1;
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                candidate = s[left+1 : right]
                if len(candidate) > len(best):
                    best = candidate
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                candidate = s[left+1 : right]
                if len(candidate) > len(best):
                    best = candidate
        return best