class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def rec(ind,arr,target):
            if ind==len(candidates):
                if target==0:
                    res.append(arr[:])
                return
            if target>0:
                arr.append(candidates[ind])
                rec(ind,arr,target-candidates[ind])
                arr.pop()
            rec(ind+1,arr,target)
        rec(0,[],target)
        return res