class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
# TAKE EXTRA TIME
        # m={}

        # for i in range(len(nums)):
        #     if nums[i] not in m:
        #         m[nums[i]]=1
        #     else:
        #         m[nums[i]]+=1
        
        # for x in m:
        #     if m[x]>(len(nums)//2):
        #         return x
# OPTIMAL

        # count=0
        # num=None

        # for i in range(len(nums)):
        #     if count==0:
        #         num=nums[i]
        #         count+=1
        #     else:
        #         if num==nums[i]:
        #             count+=1
        #         else:
        #             count-=1
        # return num
        

        num=None
        count=0

        for i in range(len(nums)):
            if count==0:
                num=nums[i]
                count+=1
            else:
                if nums[i]==num:
                    count+=1
                else:
                    count-=1
        return num