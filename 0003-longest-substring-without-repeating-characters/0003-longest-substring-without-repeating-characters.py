class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # BRUTE FORCE O(n**2)

        # maxi=0
        # n=len(s)
        # maxi=0
        # for i in range(n):
        #     m=set()
        #     for j in range(i,n):
        #         if s[j] not in m:
        #             m.add(s[j])
        #         else:
        #             break
        #         maxi=max(maxi,j-i+1) 
        # return maxi


        # maxi=0
        # n=len(s)
        # i=0
        # j=0
        # m={}
        # while j<n:
        #     if s[j] not in m:
        #         m[s[j]]=j
        #         maxi=max(maxi,j-i+1)
        #         j+=1
        #     else:
        #         i=m[s[j]]+1
        #         m[s[j]]=j
        # return maxi

        n=len(s)
        i=0
        j=0
        maxi=0
        m=set()
        while j<n:
            if s[j] not in m:
                m.add(s[j])
                j+=1
            else:
                while s[j] in m:
                    m.remove(s[i])
                    i+=1
                m.add(s[j])
                j+=1
            maxi=max(maxi,j-i)
        return maxi