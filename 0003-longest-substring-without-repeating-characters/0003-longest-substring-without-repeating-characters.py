class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        if not s:
            return 0
        m=set()
        maxi=float('-inf')
        while j<len(s):
            if s[j] not in m:
                m.add(s[j])
                maxi=max(maxi,j-i+1)
                j+=1
            else:
                while s[j] in m:
                    m.remove(s[i])
                    i+=1
        return maxi
