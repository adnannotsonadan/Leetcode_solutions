class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}

        for el in s:
            if el not in m:
                m[el] = 1
            else:
                m[el] += 1

        for i in range(len(s)):
            if m[s[i]] == 1:
                return i

        return -1
        