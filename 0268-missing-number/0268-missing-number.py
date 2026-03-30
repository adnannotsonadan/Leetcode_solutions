class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=max(nums)
        nums.sort()
        for i in range(m+1):
            if i!=nums[i]:
                return i
        return m+1
