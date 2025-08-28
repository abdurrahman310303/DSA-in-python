class Solution:
    def removeElement(self, nums, val: int) -> int:
        if not nums:
            return 0
        
        x = 0
        for num in range(len(nums)-1,-1,-1):

            if nums[num] == val:

                nums.pop(num)
            else:
                x += 1
        
        return x
        