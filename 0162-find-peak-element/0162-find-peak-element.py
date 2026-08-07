class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i=1
        j=len(nums)-2
        if len(nums)<=1:
            return 0
        if nums[0]>nums[1] :
            return 0
        if nums[-1]>nums[-2]:
            return len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            else:
                if nums[mid]<nums[mid+1]:
                    i=mid+1
                else:
                    j=mid-1
        
                
            