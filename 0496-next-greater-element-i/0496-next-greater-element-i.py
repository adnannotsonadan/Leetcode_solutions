class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # ans = []
        # for i in range(len(nums1)):
        #     f=True
        #     x = nums1[i]
        #     y = nums2.index(x)
        #     if y==len(nums2)-1:
        #         ans.append(-1)
        #         continue
        #     temp=nums2[y+1:]
        #     for j in range(len(temp)):
        #         if temp[j]>x:
        #             ans.append(temp[j])
        #             f=False
        #             break
        #     if f:
                # ans.append(-1)
        # return ans

        stack=[]
        ans=[0]*(len(nums2))
        for i in range(len(nums2)-1,-1,-1):
            while len(stack)!=0 and stack[-1]<nums2[i]:
                stack.pop()
            if len(stack)==0:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(nums2[i])
        m={}
        for i in range(len(ans)):
            m[nums2[i]]=ans[i]
        res=[]
        for i in range(len(nums1)):
            res.append(m[nums1[i]])
        return res
