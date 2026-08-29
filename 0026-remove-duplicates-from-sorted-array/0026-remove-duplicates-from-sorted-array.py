class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        k=0
        s=set()
        for i in range(n):
            if nums[i] not in s:
                s.add(nums[i])
                nums[k]=nums[i]
                k+=1
            
        return k
             