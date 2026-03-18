class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        # FOR MAX
        rnge=[0]*n
        def nge(nums):
            st=[]
            for i in range(n-1,-1,-1):
                while st and nums[st[-1]]<=nums[i]:
                    st.pop()
                if not st:
                    rnge[i]=n
                    st.append(i)
                else:
                    rnge[i]=st[-1]
                    st.append(i)
            return rnge
        nge(nums) 
        
        rpge=[0]*n
        def pge(nums):
            st=[]
            for i in range(n):
                while st and nums[st[-1]]<nums[i]:
                    st.pop()
                if not st:
                    rpge[i]=-1
                    st.append(i)
                else:
                    rpge[i]=st[-1]
                    st.append(i)
            return rpge
        pge(nums) 

        # FOR MIN
        rnse=[0]*n
        def nse(nums):
            st=[]
            for i in range(n-1,-1,-1):
                while st and nums[st[-1]]>=nums[i]:
                    st.pop()
                if not st:
                    rnse[i]=n
                    st.append(i)
                else:
                    rnse[i]=st[-1]
                    st.append(i)
            return rnse
        nse(nums) 

        rpse=[0]*n
        def pse(nums):
            st=[]
            for i in range(n):
                while st and nums[st[-1]]>nums[i]:
                    st.pop()
                if not st:
                    rpse[i]=-1
                    st.append(i)
                else:
                    rpse[i]=st[-1]
                    st.append(i)
            return rpse
        pse(nums) 
        
        minSum = 0
        maxSum = 0
        for i in range(n):

            left=i-rpse[i]
            right=rnse[i]-i
            minSum+=nums[i]*left*right
            
            left=i-rpge[i]
            right=rnge[i]-i
            maxSum+=nums[i]*left*right
        return maxSum-minSum