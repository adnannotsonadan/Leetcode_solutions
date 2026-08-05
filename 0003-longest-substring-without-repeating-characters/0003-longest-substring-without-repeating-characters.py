class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        m=set()
        i=0
        j=0
        n=len(s)
        maxi=float('-inf')
        while i<n and j<n:
            if s[j] not in m:
                m.add(s[j])
                maxi=max(maxi,j-i+1)
                j+=1
            else:
                while s[j] in m:
                    m.remove(s[i])
                    i+=1
                # maxi=max(maxi,j-i+1)
        return maxi