class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        def rec(ind,ans,tot):
            if ind==len(candidates):
                if tot==0:
                    res.append(ans[:])
                return
            
            if candidates[ind]<=tot:
                ans.append(candidates[ind])
                rec(ind,ans,tot-candidates[ind])
                ans.pop()
            rec(ind+1,ans,tot)
        rec(0,[],target)
        return res