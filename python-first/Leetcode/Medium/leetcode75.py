class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for i in range(n):
            swapped = False
            for j in range(n - i -1):
                if nums[j+1] < nums[j]:
                    nums[j+1],nums[j] = nums[j],nums[j+1]
                    swapped = True
            if not swapped:
                break       