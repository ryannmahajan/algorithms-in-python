# from pprint import pprint
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0: return 0

        sucessors = {}
        min_num = float('inf')
        max_num = float('-inf')

        for n in nums:
            if n not in sucessors: 
                sucessors[n] = 0
                min_num = min(min_num, n)
                max_num = max(max_num, n)
            
        def get_succesors(num):
            if num+1 not in sucessors: return 0

            return 1 + get_succesors(num+1)

        max_len = 1
        start = min_num
        while start <= max_num:
            curr_len = 1+ get_succesors(start)
            max_len = max(max_len, curr_len)

            start+=curr_len
        
        return max_len
        