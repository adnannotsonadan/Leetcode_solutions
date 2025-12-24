class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Brute Force
        # m=float('-inf')
        # for i in range(len(height)-1):
        #     for j in range(len(height)-1,i,-1):
        #         h=min(height[i],height[j])
        #         w=abs(i-j)
        #         a=h*w
        #         if a>m:
        #             m=a
        # return m
        i=0
        j=len(height)-1
        m=0
        while i<j:
            h=min(height[i],height[j])
            w=abs(j-i)
            a=h*w
            if a>m:
                m=a
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return m