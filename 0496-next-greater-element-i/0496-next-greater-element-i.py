class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        res=[-1]*n
        st=[]

        for i in range(n-1,-1,-1):
            while st and nums2[i]>=st[-1]:
                st.pop()
            if st:
                res[i]=st[-1]
            st.append(nums2[i])
        ans=[]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    ans.append(res[j])
        return ans
            