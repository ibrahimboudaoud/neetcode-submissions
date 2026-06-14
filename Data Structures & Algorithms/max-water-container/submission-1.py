class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        upper = len(heights)-1
        lower = 0
        while( lower < upper):
            diff = upper - lower
            tmp = min(heights[upper], heights[lower]) * diff
            if(tmp > maxVol):
                maxVol = tmp
            if(heights[lower] < heights[upper]):
                lower +=1
                while(lower < upper and heights[lower] < heights[lower-1]):
                    lower +=1
            else:
                upper -= 1
                while(lower < upper and heights[upper] < heights[upper+1]):
                    upper-=1



        return maxVol

            
        