class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        l=list(s)
        l.sort()

        for i in range(len(l)):
            nums.insert(i,l[i])
        return len(l)
        