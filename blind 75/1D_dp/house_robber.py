class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2: return max(nums)

        nums[2] += nums[0]
        ret = max(nums[1], nums[2])

        for i in range(3, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
            ret = max(ret, nums[i])
        
        return ret