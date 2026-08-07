class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=0
        h=n-1
        ans=[]
        tot=n
        while l<=h:
            mid=(l+h)//2
            print(mid)
            if nums[mid]>=target:
                tot=mid
                h=mid-1
            else:
                l=mid+1
        
        if tot==n or nums[tot]!=target:
            return [-1,-1]

        l=0
        h=n-1
        tot2=n
        while l<=h:
            mid=(l+h)//2
            if nums[mid]>target:
                tot2=mid
                h=mid-1
            else:
                l=mid+1
        return [tot,tot2-1]