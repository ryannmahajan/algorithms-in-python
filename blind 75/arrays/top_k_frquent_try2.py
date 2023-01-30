from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)

        count_to_val_list = get_count_to_val_list(count, len(nums))
        
        ret = []
        index = len(count_to_val_list) -1
        while len(ret) < k:

            ret += count_to_val_list[index]
            index -= 1
        
        return ret[:k]
            
        
def get_count_to_val_list(val_to_count, last_index):
    ret = [[] for i in range(1, last_index + 1)]

    for val, count in val_to_count.items():
        ret[count].append(val)

    return ret

# print(Solution().topKFrequent(nums = [1,1,1,2,2,2,3], k = 2))