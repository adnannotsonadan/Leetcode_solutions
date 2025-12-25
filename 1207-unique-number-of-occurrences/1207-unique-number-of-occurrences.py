class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        mn = min(arr)   
        mx = max(arr)   
        offset = -mn   
        hashed=[0]*(mx - mn + 1)
        for x in arr:
            hashed[x + offset] += 1
        sh=set(hashed)
        if sum(hashed)==sum(sh):
            return True
        else:
            return False
