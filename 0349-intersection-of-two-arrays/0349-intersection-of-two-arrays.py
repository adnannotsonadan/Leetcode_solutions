class Solution(object):
    def intersection(self, nums1, nums2):
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
        for el in m:
            if el in n:
                res.append(el)
        return res