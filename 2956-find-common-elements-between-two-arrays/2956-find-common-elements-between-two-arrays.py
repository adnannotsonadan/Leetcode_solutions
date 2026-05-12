class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m={}
        n={}

        for num in nums1:
            if num not in m:
                m[num]=1
        for num in nums2:
            if num not in n:
                n[num]=1
        res=[]
        c1=0
        for num in nums1:
            if num in nums2:
                c1+=1
        res.append(c1)
        c2=0
        for num in nums2:
            if num in nums1:
                c2+=1
        res.append(c2)
        return res
        