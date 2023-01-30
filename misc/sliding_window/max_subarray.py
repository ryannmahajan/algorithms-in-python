class Solution:
    def maxSubArray(self, nums) -> int:
        curr_sum = max_sum = nums[0]
        
        l, r = 0, 1
        LENGTH = len(nums)
        
        while r < LENGTH:
            curr_sum += nums[r]
            
            while l<=r and nums[r] > curr_sum:
                curr_sum-=nums[l]
                l+=1
            
            max_sum = max(curr_sum, max_sum)
            r+=1
        
        return max_sum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(6)
        