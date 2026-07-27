class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=float('-inf')
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                else:
                    x=(nums[i]-1)*(nums[j]-1)
                    maxi=max(maxi,x)
        return maxi