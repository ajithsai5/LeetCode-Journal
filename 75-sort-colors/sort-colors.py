class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                # Put 0 at the beginning
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # 1 is already in the correct middle area
                mid += 1

            else:  # nums[mid] == 2
                # Put 2 at the end
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1