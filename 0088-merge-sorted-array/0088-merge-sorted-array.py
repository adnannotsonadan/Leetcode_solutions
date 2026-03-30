class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(m,m+n):
        #     nums1[i]=nums2[i-m]
        # nums1.sort()

        temp=[]
        i=0
        j=0
        while i<m and j<n :
            if nums1[i]<nums2[j]:
                temp.append(nums1[i])
                i+=1
            elif nums1[i]>nums2[j]:
                temp.append(nums2[j])
                j+=1
            elif nums1[i]==nums2[j]:
                temp.append(nums1[i])
                i+=1
        while i < m:
            temp.append(nums1[i])
            i+=1
        while j < n:
            temp.append(nums2[j])
            j+=1
        nums1[:]=temp
        return nums1