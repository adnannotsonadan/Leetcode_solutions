class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # BRUTE FORCE(GIVES TLE)


        # n=len(nums)
        # nums.sort()
        # res=[]
        # for i in range(0,n):
        #     for j in range(i+1,n):
        #         tot=[]
        #         for k in range(j+1,n):
        #             if (nums[i]+nums[j]+nums[k])==0:
        #                 if [nums[i],nums[j],nums[k]] in res:
        #                     continue
        #                 res.append([nums[i],nums[j],nums[k]])
        #             else:
        #                 continue
        # return res


        res=[]
        n=len(nums)
        for i in range(0,n):
            s=set()
            for j in range(i+1,n):
                k=-(nums[i]+nums[j])
                if k not in s:
                    s.add(nums[j])
                else:
                    if sorted([nums[i],nums[j],k]) not in res:
                        res.append(sorted([nums[i],nums[j],k]))
                    else:
                        continue
        return res
                    


