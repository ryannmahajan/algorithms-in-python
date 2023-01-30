class Solution:
    def threeSum(self, nums) -> List[List[int]]:
        res = []

        for a, i in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue

            l, r = i+1, len(nums) -1

            while l < r:
                b, c = nums[l], nums[r]
                if b+c==-a:
                    res.append([a, b, c])
                    l+=1

                    while nums[l]==nums[l-1] and l < r:
                        l+=1

                elif b+c > -a:
                    r-=1
                else:
                    l+=1        

        return res
        