class Solution:
    def removeDuplicates(self, nums) -> int:

        if not nums:
            return
        
        x = 0

        for i in range(1, len(nums)):

            if nums[i] != nums[x]:

                x = x+1
                nums[x] = nums[i]
        return x + 1
                

        