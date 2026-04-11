class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        m={}
        res=[]
        for i in range(n):
            s=target-numbers[i]
            if s not in m:
                m[numbers[i]]=i
            else:
                res.append(m[s]+1)
                res.append(i+1)
        return res