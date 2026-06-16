class Solution:
    def reverse(self, x: int) -> int:
        text = str(x)
        removed_char = ''
        if text[0] == '-':
            removed_char = text[0]
            text = text[1:]
        reversed_text = text[::-1]
        reversed_text = removed_char + reversed_text
        result = int(reversed_text)

        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result