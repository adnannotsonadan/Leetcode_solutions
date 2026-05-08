class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n=len(nums)
        # arr=[0]*n
        # for i in range(n):
        #     prod=1
        #     for j in range(n):
        #         if i==j:
        #             continue
        #         else:
        #             prod*=nums[j]
        #     arr[i]=prod
        # return arr

        n=len(nums)
        left=[0]*n
        left[0]=1
        right=[0]*n
        right[n-1]=1

        for i in range(1,n):
            left[i]=nums[i-1]*left[i-1]
        
        for i in range(n-2,-1,-1):
            right[i]=nums[i+1]*right[i+1]
        
        arr=[0]*n
        for i in range(n):
            arr[i]=left[i]*right[i]
        return arr

