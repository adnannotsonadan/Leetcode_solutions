class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        hash={}
        for i in range(n):
            if nums[i]  in hash:
                hash[nums[i]]+=1
            else:
                hash[nums[i]]=1
                
        for i in range(n):
            if hash[nums[i]]==1:
                return nums[i]
            
        