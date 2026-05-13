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

        # temp=[]
        # i=0
        # j=0
        # while i<m and j<n :
        #     if nums1[i]<nums2[j]:
        #         temp.append(nums1[i])
        #         i+=1
        #     elif nums1[i]>nums2[j]:
        #         temp.append(nums2[j])
        #         j+=1
        #     elif nums1[i]==nums2[j]:
        #         temp.append(nums1[i])
        #         i+=1
        # while i < m:
        #     temp.append(nums1[i])
        #     i+=1
        # while j < n:
        #     temp.append(nums2[j])
        #     j+=1
        # nums1[:]=temp
        # return nums1


        # NO EXTRA SPACE APPROACH

        # i=m-1   #nums1
        # j=n-1  #nums2
        # k=m+n-1

        # if m==0:
        #     nums1[:]=nums2
        # while i>=0 and j>=0:
        #     if nums2[j]>nums1[i]:
        #         nums1[k]=nums2[j]
        #         j-=1
        #         k-=1
        #     elif nums2[j]<nums1[i]:
        #         nums1[k]=nums1[i]
        #         i-=1
        #         k-=1
        #     elif nums2[j]==nums1[i]:
        #         nums1[k]=nums1[i]
        #         i-=1
        #         k-=1
        # while j>=0:
        #     nums1[k]=nums2[j]
        #     j-=1
        #     k-=1
        # return nums1

        i=0
        j=0
        k=[]
        while i!=m and j!=n:
            if nums1[i]<=nums2[j]:
                k.append(nums1[i])
                i+=1
            else:
                k.append(nums2[j])
                j+=1
        while i<m:
            k.append(nums1[i])
            i+=1
        
        while j<n:
            k.append(nums2[j])
            j+=1
        nums1[:]=k