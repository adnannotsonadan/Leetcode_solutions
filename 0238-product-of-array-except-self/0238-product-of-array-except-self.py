class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[0]*n
        left[0]=1
        prod1=1

        for i in range(1,n):
            prod1*=nums[i-1]
            print(prod1)
            left[i]=prod1
        
        right=[0]*n
        right[n-1]=1

        prod2=1
        for i in range(n-2,-1,-1):
            prod2*=nums[i+1]
            right[i]=prod2
        res=[0]*n
        for i in range(n):
            res[i]=left[i]*right[i]
        return res