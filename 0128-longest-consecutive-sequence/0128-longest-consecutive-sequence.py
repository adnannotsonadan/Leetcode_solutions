class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # BRUTE FORCE
        # n=len(nums)
        # maxi=0

        # for i in range(n):
        #     num=nums[i]
        #     count=1
        #     while num+1 in nums:
        #         count+=1
        #         num+=1
        #     maxi=max(maxi,count)
        # return maxi

        # OPTIMAL
        n=len(nums)
        s=set()
        maxi=0
        for num in nums:
            s.add(num)
        for num in s:
            count=1
            if num-1 not in s:
                while num+1 in s:
                    count+=1
                    num+=1
                maxi=max(maxi,count)
            else:
                continue
        return maxi
                

