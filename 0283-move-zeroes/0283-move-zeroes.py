class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # res=[]
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         res.append(nums[i])
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         res.append(nums[i])
        # nums[:]=res
        # return nums

        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i]=0
        return nums