class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=sum(nums)
        l=len(nums)
        x=0
        for i in range(1,l+1):
            x+=i
        return abs(x-s)
