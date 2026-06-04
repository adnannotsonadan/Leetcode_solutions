class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BRUTE FORCE
        # n=len(nums)
        # m={}
        # for i in range(n):
        #     if nums[i] not in m:
        #         m[nums[i]]=1
        #     else:
        #         m[nums[i]]+=1
        
        # for key in m:
        #     if m[key]>1:
        #         return key
         
        # Another approach
        # n=len(nums)
        # s=set()
        # for el in nums:
        #     if el in s:
        #         return el
        #     else:
        #         s.add(el)
        
        # OPTIMAL APPROACH NO EXTRA SPACE
        nums.sort()
        prev=nums[0]
        curr=nums[1]

        for i in range(1,len(nums)):
            curr=nums[i]
            if curr==prev:
                return curr
            prev=nums[i]
        

        