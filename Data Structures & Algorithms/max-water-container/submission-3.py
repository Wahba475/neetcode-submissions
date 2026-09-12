class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res=0
        r=len(heights)-1
        l=0
        while l<r:
            result=(r-l)*min(heights[l],heights[r])
            res=max(res,result)
            if (heights[l]>heights[r]):
                r-=1
            else:
                l+=1
        return res        

                

              

        