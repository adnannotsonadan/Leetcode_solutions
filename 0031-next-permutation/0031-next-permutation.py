class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ind=None
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                ind=i-1
                break
        if ind is None:
            nums.reverse()
            return
        
        x=ind
        for j in range(len(nums)-1,ind,-1):
            if nums[j]>nums[ind]:
                nums[j],nums[ind]=nums[ind],nums[j]
                break
        
        nums[ind+1:]=nums[ind+1:][::-1]