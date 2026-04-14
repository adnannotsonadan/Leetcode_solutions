class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m={}
        maxi=0
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]]=1
                
            else:
                m[nums[i]]+=1
        maxi=0    
        for x in m:
            maxi=max(maxi,m[x])
        c=0
        for i in range(len(nums)):
            if m[nums[i]]==maxi:
                c+=1
        return c