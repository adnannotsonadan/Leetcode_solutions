class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total=sum(nums)
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0

        s = (target + total) // 2 
        n=len(nums)
        def rec(ind,target):
            if ind==0:
                if target==0 and nums[0]==0:
                    return 2
                if target==0 or target == nums[0]:
                    return 1
                return 0
            nt=rec(ind-1,target)
            take=0
            if nums[ind]<=target:
                take=rec(ind-1,target-nums[ind])
            return take+nt
        return rec(n-1,s)