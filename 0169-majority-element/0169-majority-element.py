class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m={}
        maxi=None
        for num in nums:
            if num not in m:
                m[num]=1
            else:
                m[num]+=1
        x=sorted(m.items(),key=lambda x:x[1],reverse=True)
        return x[0][0]            