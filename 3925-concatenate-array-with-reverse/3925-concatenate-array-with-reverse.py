class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        temp=[0]*(2*n)
        c=0
        for i in range(n):
            temp[i]=nums[i]
            c+=1

        nums=nums[::-1]
        
        for i in range(n):
            temp[c]=nums[i]
            c+=1
        return temp
