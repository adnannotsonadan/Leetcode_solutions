class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        temp=[]
        def rec(ind,target,arr):
            if target==0:
                temp.append(arr[:])
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                arr.append(candidates[i])
                rec(i+1,target-candidates[i],arr)
                arr.pop()
        rec(0,target,[])
        return temp