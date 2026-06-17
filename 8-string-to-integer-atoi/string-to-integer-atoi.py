class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        results =""
        while i < n and s[i] == ' ':
            i += 1
        sign = 1
        if i < n and s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        result = sign * result
        return max(MIN_INT, min(result, MAX_INT))