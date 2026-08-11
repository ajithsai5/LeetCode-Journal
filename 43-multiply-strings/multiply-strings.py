class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle zero
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        # Multiply digit by digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        # Convert array to string
        start = 0

        while start < len(result) and result[start] == 0:
            start += 1

        return ''.join(str(x) for x in result[start:])