class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ls[0]=1
        # for i in range(1,n):
        #     ls[i]=ls[i-1]+nums[i]
        # return ls
        n=len(nums)
        ls=[0]*n
        s=sum(nums)
        s1=sum(nums)
        for i in range(n-1,-1,-1):
            s=s-nums[i]
            ls[i]=s
        rs=[0]*n
        for i in range(n):
            s1=s1-nums[i]
            rs[i]=s1
        
        for i in range(n):
            if ls[i]==rs[i]:
                return i
        return -1
