class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        maxi=0
        i=0
        j=n-1

        while i<j:
            width=j-i
            h=min(height[i],height[j])
            maxi=max(maxi,width*h)
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        return maxi