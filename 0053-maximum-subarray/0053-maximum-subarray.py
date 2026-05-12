class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n=len(nums)
        # maxi=float('-inf')
        # for i in range(0,n):
        #     tot=0
        #     for j in range(i,n):
        #         tot+=nums[j]
        #         maxi=max(maxi,tot)
        # return maxi

        n=len(nums)
        maxi=float('-inf')
        tot=0

        for i in range(n):
            tot+=nums[i]
            maxi=max(maxi,tot)
            if tot<0:
                tot=0
        return maxi
        