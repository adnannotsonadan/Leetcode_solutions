class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n=len(s)
        # maxi=0
        
        # for i in range(n):
        #     m=set()
        #     for j in range(i,n):
        #         if s[j] not in m:
        #             m.add(s[j])
        #             maxi=max(maxi,len(m))
        #         else:
        #             break
        # return maxi


        maxi=0
        i=0
        j=0
        n=len(s)
        m=set()
        while i<n:
            if j<n:
                if s[j] not in m:
                    m.add(s[j])
                    maxi=max(maxi,j-i+1)
                    j+=1
                else:
                    while s[j] in m:
                        m.remove(s[i])
                        i+=1
            else:
                i+=1
        return maxi