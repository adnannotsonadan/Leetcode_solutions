class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        subs = []
        def isPal(pal):
            if pal==pal[::-1]:
                return True
            else:
                return False
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if isPal(s[i:j]):
                    subs.append(s[i:j])
                else:
                    continue
        return len(subs)
        