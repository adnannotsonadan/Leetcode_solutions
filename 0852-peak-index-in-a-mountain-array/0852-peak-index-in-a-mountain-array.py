class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        left=[0]*n
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                left[i]=arr[i+1]
        
        right=[0]*n
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                right[i]=arr[i-1]
        
        for i in range(1,n-1):
            if arr[i]==left[i-1] and arr[i]==right[i+1]:
                return i