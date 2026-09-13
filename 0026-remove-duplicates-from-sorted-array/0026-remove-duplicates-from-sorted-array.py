class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        s=set()
        for i in range(len(nums)):
            if nums[i] not in s:
                nums[k]=nums[i]
                k+=1
                s.add(nums[i])
        return k