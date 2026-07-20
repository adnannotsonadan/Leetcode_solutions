class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m):
            nums2.append(nums1[i])
        nums2.sort()
        for i in range(m+n):
            nums1[i]=nums2[i]

        
