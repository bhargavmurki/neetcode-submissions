class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortnums = sorted(set(nums))
        longest = 1
        cur = 1

        if not nums:
            return 0

        for i in range(len(sortnums) - 1):
            if sortnums[i + 1] - sortnums[i] == 1:
                cur +=1
            else:
                longest = max(longest, cur)
                cur = 1
        return max(longest, cur)