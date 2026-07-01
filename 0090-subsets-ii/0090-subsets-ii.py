class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        n=len(nums)
        nums.sort()
        def rec(ind,ans):
            if ind==n:
                if ans in res:
                    return
                res.append(ans[:])
                return
            ans.append(nums[ind])
            rec(ind+1,ans)
            ans.pop()
            rec(ind+1,ans)
        rec(0,[])
        return res