class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        ans=nums[0]
        maxi=0
        for i in range(1,len(nums)):
            ans+=nums[i]
            maxi=max(maxi,ans)
            if ans<0:
                ans=0
            
            
        return maxi