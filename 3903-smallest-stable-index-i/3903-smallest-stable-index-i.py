class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        lm=[0]*n
        lm[0]=nums[0]
        for i in range(1,n):
            lm[i]=max(lm[i-1],nums[i])

        rm=[0]*n
        rm[n-1]=nums[-1]
        for i in range(n-2,-1,-1):
            rm[i]=min(rm[i+1],nums[i])

        for i in range(n):
            if abs(rm[i]-lm[i])<=k:
                return i
        return -1