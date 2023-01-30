class Solution:
    def twoSum(self, numbers, target):
        start, end = 0, len(numbers) - 1

        while start != end:
            a, b = numbers[start], numbers[end]
            if a+b==target:
                break
            elif a+b > target:
                end-=1
            else:
                start+=1

        return [start+1, end+1]
        