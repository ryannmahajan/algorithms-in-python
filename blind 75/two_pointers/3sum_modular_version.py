class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        ret = []
        i = 0
        while i < len(nums):
            value = nums[i]

            pairs = get_two_sum_lists(-value, nums, i+1, len(nums) -1 )
            ret += add_value_to_pairs(pairs, value)

            i = val_of_next_unique_index(nums, i)

        return ret
        

def get_two_sum_lists(target, arr, l, r):
    ret = []
    while l < r and l < len(arr):
        l_val, r_val = arr[l], arr[r]

        if l_val + r_val == target:
            ret.append([l_val, r_val])
            l = val_of_next_unique_index(arr, l)
        
        elif l_val + r_val < target:
            l = val_of_next_unique_index(arr, l)
        
        else:
            r-=1

    return ret

def val_of_next_unique_index(arr, i):
    i += 1

    while i < len(arr) and arr[i]==arr[i-1]:
        i += 1
    
    return i

def add_value_to_pairs(pairs, value):
    return [[pair[0], pair[1], value] for pair in pairs]