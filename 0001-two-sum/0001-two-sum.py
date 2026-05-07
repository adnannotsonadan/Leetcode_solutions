class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # temp=[]
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             temp.append(i) 
        #             temp.append(j) 
        #         else:
        #             continue
        # return temp
        # n=len(nums)
        # m={}
        # res=[]
        # for i in range(n):
        #     x=target - nums[i]
        #     if x not in m:
        #         m[nums[i]]=i
        #     else:
        #         res.append(m[x])
        #         res.append(i)
        # return res

        m={}
        res=[]
        for i in range(len(nums)):
            x=target-nums[i]
            if x not in m:
                m[nums[i]]=i
            else:
                res.append(m[x])
                res.append(i)
        return res

            
                
        