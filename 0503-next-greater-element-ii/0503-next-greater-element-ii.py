class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=[]
        n=len(nums)
        ans=[0]*(len(nums))
        for i in range((2*n)-1,-1,-1):
            while len(st)!=0 and st[-1]<=nums[i%n]:
                st.pop()
            if len(st)==0:
                if i<n:
                    ans[i]=-1
            else:
                if i<n:
                    ans[i]=st[-1]
            st.append(nums[i%n])
        return ans