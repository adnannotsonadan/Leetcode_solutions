class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxi=float('-inf')
        n=len(heights)
        res1=[0]*n
        def nse(heights):
            st=[]
            for i in range(n-1,-1,-1):
                while st and heights[st[-1]]>=heights[i]:
                    st.pop()
                if not st:
                    res1[i]=n
                else:
                    res1[i]=st[-1]
                st.append(i)
            return res1
        nse(heights)
        res2=[0]*n
        def pse(heights):
            st=[]
            for i in range(n):
                while st and heights[st[-1]]>heights[i]:
                    st.pop()
                if not st:
                    res2[i]=-1
                else:
                    res2[i]=st[-1]
                st.append(i)
            return res2
        pse(heights)

        for i in range(n):
            width=res1[i]-res2[i]-1
            maxi=max(maxi,heights[i]*width)
        return maxi
