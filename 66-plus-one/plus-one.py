class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):

            # If digit is less than 9, just add 1
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # 9 becomes 0, carry 1 to the left
            digits[i] = 0

        # If we reach here, every digit was 9
        return [1] + digits