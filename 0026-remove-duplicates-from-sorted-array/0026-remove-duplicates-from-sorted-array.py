class Solution(object):
    def removeDuplicates(self, nums):
        
        # s=set(nums)
        # l=list(s)
        # l.sort()
        # for i in range(len(s)):
        #     nums.insert(i,l[i])

        # return len(l)
        
        # length=0
        # hash=[0]*(len(nums))
        # for x in nums:
        #     hash[x]=hash[nums[x]]+1
        # for i in range(1,len(hash)):
        #     if hash[i]>0:
        #         length+=1
        # return length

        # s=set()
        # nums=list(s)
        # # for x in nums:
        # #     s.add(x)
        # return len(nums)

        seen=set()
        k=0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[k]=nums[i]
                k+=1
        return k