class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums:
            return [-1,-1]
        n=len(nums)
        low=0
        high=n-1

        ans=n
        res=[]
        while low<=high:
            mid=low+(high-low)//2

            if nums[mid]>=target:
                ans=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
        if ans==n or nums[ans]!=target:
            return [-1,-1]
        
        first=ans
        
        ans1=n
        low1=0
        high1=n-1

        while low1<=high1:
            mid1=low1+(high1-low1)//2
            if nums[mid1]>target:
                ans1=mid1
                high1=mid1-1
            else:
                low1=mid1+1
        if ans1==n:
            last=n-1
        else:
            last=ans1-1
        return [first,last]