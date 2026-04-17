class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # USING 2 POINTES

        i=0
        j=1

        while j<len(nums):
            if nums[i]!=nums[j]:
                i+=1
                nums[i]=nums[j]
                j+=1
            elif nums[i]==nums[j]:
                j+=1
            
        return i+1