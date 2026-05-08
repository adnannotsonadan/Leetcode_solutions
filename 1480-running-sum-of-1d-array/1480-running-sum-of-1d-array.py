class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        left=[0]*n
        left[0]=nums[0]

        for i in range(1,n):
            left[i]=left[i-1]+nums[i]
        return left

        