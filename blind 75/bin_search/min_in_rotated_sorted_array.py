
class Solution:
    def findMin(self, nums: list[int]) -> int:
        return self.find_min_helper(nums, 0, len(nums)-1)
    
    def find_min_helper(self, nums, l, r):
        if l==r:
            return nums[l]
        
        m = (l+r)//2 #floor

        left, mid, right = nums[l], nums[m], nums[r]

        if left <= mid:
            if right < mid:
                return self.find_min_helper(nums, m+1, r)
            else:
                return left
        else:
            if nums[m-1] > mid:
                return mid
            else:
                return self.find_min_helper(nums, l, m)

