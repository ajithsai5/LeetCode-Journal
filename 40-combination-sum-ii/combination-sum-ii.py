class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted, no later number can work
                if candidates[i] > target:
                    break

                path.append(candidates[i])

                # i + 1 because each element can only be used once
                backtrack(i + 1, target - candidates[i], path)

                path.pop()

        backtrack(0, target, [])
        return result