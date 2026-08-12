class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0

        star = -1
        match = 0

        while i < len(s):

            # Normal character or '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1

            # '*'
            elif j < len(p) and p[j] == '*':
                star = j
                match = i

                # Initially let '*' match empty
                j += 1

            # Mismatch, but we have seen '*'
            elif star != -1:
                j = star + 1

                # Let '*' match one more character
                match += 1
                i = match

            # Mismatch and no '*'
            else:
                return False

        # Remaining pattern must contain only '*'
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)