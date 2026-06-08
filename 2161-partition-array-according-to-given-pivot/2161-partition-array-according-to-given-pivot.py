class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left=[]
        right=[]

        for i in range(len(nums)):
            if nums[i]<pivot:
                left.append(nums[i])
            
        for i in range(len(nums)):
            if nums[i]>pivot:
                right.append(nums[i])
        
        for i in range(len(nums)):
            if nums[i]==pivot:
                left.append(pivot)
        
        left.extend(right)
        return left
