class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        t = 0
        for i in range(len(nums)):
            if nums[i] != val: 
                nums[t] = nums[i]
                t += 1
        return t