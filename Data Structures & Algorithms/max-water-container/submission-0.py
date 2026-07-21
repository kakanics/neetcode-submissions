class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        area = 0

        while l<r:
            x = r-l
            y = min(heights[l], heights[r])
            _area = x*y
            area = max(area, _area)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return area