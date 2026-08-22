class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        d=k%n

        res=[]

        nums[:]=nums[n-d:]+nums[:n-d]
        return nums