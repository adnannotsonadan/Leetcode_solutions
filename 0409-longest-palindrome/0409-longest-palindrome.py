class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=set()
        l=0
        for i in range(len(s)):
            if s[i] not in m:
                m.add(s[i])
            else:
                l+=2
                m.remove(s[i])
        if m:
            l+=1
        return l
