class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        right=0
        n=len(s)
        maxi=0
        d={}
        while right<n:
            if s[right] not in d:
                d[s[right]]=right
            else:
                left=max(left,d[s[right]]+1)
            d[s[right]]=right
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi

        