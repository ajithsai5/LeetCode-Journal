class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            # We have a complete permutation
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                # Already used in current permutation
                if used[i]:
                    continue

                # Choose
                path.append(nums[i])
                used[i] = True

                # Explore
                backtrack()

                # Undo
                used[i] = False
                path.pop()

        backtrack()
        return result