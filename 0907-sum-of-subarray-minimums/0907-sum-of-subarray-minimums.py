class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # n=len(arr)
        # MOD=10**9 +7
        # s=0
        # for i in range(n):
        #     res=[]   
        #     for j in range(i,n):
        #         res.append(arr[j])
                
        #         s+=min(res)%MOD
        # return s
        n=len(arr)
        res1=[0]*n
        def nse(arr):
            st=[]
            for i in range(n-1,-1,-1):
                while st and arr[st[-1]]>=arr[i]:
                    st.pop()
                if not st:
                    res1[i]=n
                    st.append(i)
                else:
                    res1[i]=st[-1]
                    st.append(i)
            return res1
        nse(arr)
        res2=[0]*n
        def pse(arr):
            st=[]
            for i in range(n):
                while st and arr[st[-1]]>arr[i]:
                    st.pop()
                if not st:
                    res2[i]=-1
                    st.append(i)
                else:
                    res2[i]=st[-1]
                    st.append(i)
            return res2
        pse(arr)
        total=0
        MOD = 10**9 + 7
        for i in range(n):
            x=i-res2[i]
            y=res1[i]-i
            total=(total+arr[i]*x*y)%MOD
        return total