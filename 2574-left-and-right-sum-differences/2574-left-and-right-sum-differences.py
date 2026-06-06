class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        left=[0]*n
        s1=0
        right=[0]*n
        s2=0

        for i in range(1,n):
            left[i]=s1+nums[i-1]
            s1=left[i]
        
        for j in range(n-2,-1,-1):
            right[j]=s2+nums[j+1]
            s2=right[j]
        res=[0]*n

        for i in range(n):
            res[i]=abs(left[i]-right[i])
        return res
