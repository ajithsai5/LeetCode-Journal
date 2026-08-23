class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Convert k to 0-based index
        k -= 1

        result = []

        for i in range(n, 0, -1):
            block_size = self.factorial(i - 1)

            index = k // block_size
            k = k % block_size

            result.append(numbers.pop(index))

        return ''.join(result)

    def factorial(self, n: int) -> int:
        result = 1

        for i in range(2, n + 1):
            result *= i

        return result