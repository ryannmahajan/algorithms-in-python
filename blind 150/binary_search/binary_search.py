from math import floor

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return search_helper(nums, target, 0, len(nums)-1)
    
def search_helper(nums, target, start, end):
    if start==end:
        return start if nums[start]==target else -1
    
    mid = floor((start+end)/2)
    
    found = nums[mid]

    if found == target:
        return mid
    elif target < found:
        return search_helper(nums, target, start, mid)
    else: return search_helper(nums, target, mid+1, end)
     
    

