class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0

        def area_of_vals(i1, i2):
            return (i2-i1)*min(height[i1], height[i2])

        while l<r:
            max_area = max(max_area, area_of_vals(l, r))
        if height[l] < height[r]:
            l+=1
        else: 
            r+=1

        return max_area

        # for i in (1, len(height)): 
        #   if area_of_vals(l, i) > max_area: 
        #     max_area =  area_of_vals(l, i)
        #     r = i
        # for i in (0, r): 
        #   if area_of_vals(i, r)> max_area:
        #     max_area =  area_of_vals(i, r)
        #     l = i
        # return max_area

