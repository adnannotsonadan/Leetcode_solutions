class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n=len(matrix[0])
        def largestRect(arr):

            res1=[0]*n
            def nse(arr):
                st=[]
                for i in range(n-1,-1,-1):
                    while  st and arr[st[-1]]>=arr[i]:
                        st.pop()
                    if not st:
                        res1[i]=n
                    else:
                        res1[i]=st[-1]
                    st.append(i)
                return res1
            nse(arr)
            res2=[0]*n
            def pse(arr):
                st=[]
                for i in range(n):
                    while  st and arr[st[-1]]>arr[i]:
                        st.pop()
                    if not st:
                        res2[i]=-1
                    else:
                        res2[i]=st[-1]
                    st.append(i)
                return res2
            pse(arr)
            maxi=float('-inf')
            for i in range(n):
                width=res1[i]-res2[i]-1
                maxi=max(maxi,arr[i]*width)
            return maxi
            

        maxi1=[0]
        def maxRect(matrix):
            n=len(matrix)
            m=len(matrix[0])
            height=[0]*m
            if not matrix:
                return 0
            
            for i in range(n):
                for j in range(m):
                    if matrix[i][j]=='1':
                        height[j]+=1
                    else:
                        height[j]=0
                maxi1[0]=max(maxi1[0],largestRect(height))
        maxRect(matrix)
        return maxi1[0]