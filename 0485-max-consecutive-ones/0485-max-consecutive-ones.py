class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        m=0
        for i in range(len(nums)):
            if nums[i]==1:
                k+=1
                m=max(m,k)
            elif nums[i]!=1:
                k=0
        return m