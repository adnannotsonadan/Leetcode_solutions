class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        op=0
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]+nums[j]<k:
                i+=1
            
            elif nums[i]+nums[j]>k:
                j-=1
            elif nums[i]+nums[j]==k:
                op+=1
                i+=1
                j-=1
        return op
            