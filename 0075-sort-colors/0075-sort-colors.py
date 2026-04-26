class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r=0
        w=0
        b=0

        for x in nums:
            if x==0:
                r+=1
            elif x==1:
                w+=1
            elif x==2:
                b+=1
        for i in range(r):
            
            nums[i]=0
            
        for i in range(r,r+w):
            
            nums[i]=1
            
        for i in range(w+r,r+w+b):
            
            nums[i]=2
        return nums
            