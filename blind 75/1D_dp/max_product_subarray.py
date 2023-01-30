class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        max_pos = [0] * len(nums)
        max_neg = [0] * len(nums)

        for i, num in enumerate(nums):
            temp = num

            if i!=0:
                is_previous_positive = max_pos[i-1] > 0
                temp *= (max_pos[i-1] if is_previous_positive else max_neg[i-1])

            res = max(res, temp)

            if temp > 0:
                max_pos[i] = temp
            else:
                max_neg[i] = temp
        
        return res