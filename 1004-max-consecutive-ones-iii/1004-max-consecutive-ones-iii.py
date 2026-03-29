class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # BRUTE FORCE
        # maxi=0
        # for i in range(len(nums)):
        #     j=i
        #     r=0
        #     c=0
        #     while j<len(nums) and r<=k:
        #         if nums[j]==0:
        #             r+=1
        #         if r>k:
        #             break
        #         c+=1
        #         j+=1
        #     maxi=max(maxi,c)
        # return maxi 


        # OPTIMAL
        # l=0
        # r=0
        # n=len(nums)
        # zeros=0
        # maxi=0
        # while r<n:
        #     if nums[r]==0:
        #         zeros+=1
        #     while zeros>k:
        #         if nums[l]==0:
        #             zeros-=1
        #         l+=1
        #     if zeros<=k:
        #         maxi=max(maxi,r-l+1)
        #     r+=1
        # return maxi

        l=0
        r=0
        maxi=0
        n=len(nums)
        z=0
        while r<n:
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi