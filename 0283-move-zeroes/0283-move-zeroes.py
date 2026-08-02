class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                continue
            if nums[i]!=0:
                nums[temp]=nums[i]
                temp+=1
        for i in range(temp,n):
            nums[i]=0
        