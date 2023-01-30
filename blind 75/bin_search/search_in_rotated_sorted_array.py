class Solution:

    def search(self, nums: list[int], target: int) -> int:
        self.nums = nums
        self.target = target

        return self.search_helper(0, -1)

    def search_helper(self, l_index, r_index):
        nums, target = self.nums, self.target

        l, r = nums[l_index], nums[r_index]
        if l==r:
            return l_index if l==target else -1

        m = nums[int(l_index+r_index/2)]

        if m_in_upper_curve(m, l, r):
            if between(l, target, m):
                return self.search_helper(l, m)
            else:
                return self.search_helper(m, r)
        
        else:
            if between(m, target, r):
                return self.search_helper(m, r)
            else:
                return self.search_helper(l, m)
    
def m_in_upper_curve(m, l, r):
    return (l <= m) and (r < m)

def between(l, candidate, r):
    return l <= candidate <= r

print(Solution().search(nums = [4,5,6,7,0,1,2], target = 0))