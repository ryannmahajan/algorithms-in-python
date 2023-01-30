class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        res = 0
        prod = 1

        l, r = 0, 0
        LENGTH = len(nums)

        # print(f"k={k}")
        # print(f"list = {nums[l:r]}, prod = {prod}")

        while (r<LENGTH):
            prod*=nums[r]
            # print(f"list = {nums[l:r+1]}, prod = {prod}")

            # knowing that it will iterate forward even if first couple values are too big
            while l <= r and prod >= k:
                prod/=nums[l]

                l+=1
                # print(f"list = {nums[l:r+1]}, prod = {prod}")

                # print(f"l={l}")


            if prod < k:
                res += r-l+1

            r+=1
            # print(f"list = {nums[l:r+1]}, prod = {prod}")

            # print(f"r={r}")

        
        return res

print(Solution().numSubarrayProductLessThanK([1000, 2,999, 3], 1000))
