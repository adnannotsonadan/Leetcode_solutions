class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m={}

        for num in nums:
            if num not in m:
                m[num]=1
            else:
                m[num]+=1
        for key in m:
            if m[key]>1:
                return True
        return False