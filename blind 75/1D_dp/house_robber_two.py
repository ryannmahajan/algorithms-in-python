class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums: list[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        
        first, second, third = nums[0], nums[1], nums[0] + nums[2]
        for num in nums[3:]:
            first, second, third = second, third, max(first, second) + num
        
        return max(second, third)
        

# print(Solution().rob([200,3,140,20,10]))