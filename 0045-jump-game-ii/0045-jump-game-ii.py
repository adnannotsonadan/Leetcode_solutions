class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        j=0
        while r<len(nums)-1:
            furtherest=0
            for i in range(l,r+1):
                furtherest=max(furtherest,i+nums[i])
            l=r+1
            r=furtherest
            j+=1
        return j