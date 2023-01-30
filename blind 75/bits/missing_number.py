class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        
        a = 0
        for i in range(n+1): a ^= i

        for num in nums: a^= num

        return a
