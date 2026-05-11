class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        m={}

        for i in range(len(numbers)):
            x=target-numbers[i]
            if x not in m:
                m[numbers[i]]=i
            else:
                return [m[x]+1,i+1]
        
        