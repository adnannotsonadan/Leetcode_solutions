class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        # l=0
        # r=0
        # res=[]
        n=len(nums)
        # s=0
        # while r<n:
        #     s+=nums[r]
        #     while s>target:
        #         s-=nums[l]
        #         l+=1
        #     if s==target:
        #         break
        #     r+=1
        # res.append(l)
        # res.append(r)
        # return res
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        # i=0
        # j=0
        # res=[]
        # m={}
        # for i in range(len(nums)):
        #     if nums[i] not in m:
        #         m[nums[i]]=i
        #     else:
        #         m[nums[i]]=i
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             res.append(i)
        #             res.append(j)
        # return res


        # OPTIMAL APPROACH

        m={}
        n=len(nums)
        res=[]
        for i in range(n):
            s=target-nums[i]
            if s not in m:
                m[nums[i]]=i
            else:
                res.append(m[s])
                res.append(i)
        return res