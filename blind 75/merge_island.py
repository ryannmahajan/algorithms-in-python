
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key= lambda x: x[0])
        ans = []
        
        for i in range(len(intervals)-1):
            first, second = intervals[i], intervals[i+1]
            
            if do_intervals_overlap(first, second):
                intervals[i+1] = merged_interval(first, second)
            else:
                print(f"intervals[i] = {intervals[i]}")
                ans.append(first)
        
        return ans
    
def do_intervals_overlap(first, second):
    return first[1] >= second[0]
    
def merged_interval(first, second):
    return [first[0], max(first[1], second[1])]
    

a = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(a))
