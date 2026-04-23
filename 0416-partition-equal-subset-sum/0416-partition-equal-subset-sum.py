class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # total=sum(nums)
        # n=len(nums)
        # if total%2!=0:
        #     return False
        # else:
        #     target=total//2
        # dp=[[-1]*(target+1) for _ in range(n)]
        
        # def rec(ind,target):
        #     if target==0:
        #         return True
            
        #     if ind==0:
        #         if nums[ind]==target:
        #             return True
        #         return False
        #     if dp[ind][target]!=-1:
        #         return dp[ind][target]
        #     not_take=rec(ind-1,target)
        #     take=False
        #     if nums[ind]<=target:
        #         take=rec(ind-1,target-nums[ind])
        #     dp[ind][target] = take or not_take
        #     return dp[ind][target]
        # return rec(n-1,target)

        n=len(nums)
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        dp=[[-1]*(target+1) for _ in range(n)]

        def rec(ind,target):
            if target==0:
                return True
            if ind==0:
                if target==0:
                    return True
                return False
            if dp[ind][target]!=-1:
                return dp[ind][target]
            np=rec(ind-1,target)
            pick=0
            if nums[ind]<=target:
                pick=rec(ind-1,target-nums[ind])
            dp[ind][target]=pick or np
            return dp[ind][target]
        return rec(n-1,target)