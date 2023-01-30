from operator import mod
from math import floor

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        self.ROWS, self.COLS = len(matrix), len(matrix[0])

        return self.search_helper(matrix, target, 0, self.get_last_index())!=-1

    def search_helper(self, matrix, target, start, end):
        print(f"Start={start}, end={end}")
        if start==end:
            return start if self.get_val_at(matrix, start)==target else -1
        
        mid = floor((start+end)/2)
        
        found = self.get_val_at(matrix, mid)

        if found == target:
            return mid
        elif target < found:
            return self.search_helper(matrix, target, start, mid)
        else: return self.search_helper(matrix, target, mid+1, end)
        
    def get_val_at(self, matrix, index):
        return matrix[index//self.COLS][mod(index, self.COLS)]
    
    def get_last_index(self):
        return self.ROWS*self.COLS - 1

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
print(Solution().searchMatrix(matrix, target))