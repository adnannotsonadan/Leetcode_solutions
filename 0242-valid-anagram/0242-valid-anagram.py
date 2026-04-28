class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # bf

        # return sorted(s)==sorted(t)

        # optimal
        # m={}
        # n={}

        # if len(s)!=len(t):
        #     return False
        
        # for i in range(len(s)):
        #     if s[i] not in m:
        #         m[s[i]]=1
        #     else:
        #         m[s[i]]+=1
        # for i in range(len(t)):
        #     if t[i] not in n:
        #         n[t[i]]=1
        #     else:
        #         n[t[i]]+=1
        
        # if m==n:
        #     return True
        # else:
        #     return False

        m={}
        if len(s)!=len(t):
            return False
        for x in s:
            if x not in m:
                m[x]=1
            else:
                m[x]+=1
        for i in range(len(t)):
            if t[i] not in m:
                return False
            m[t[i]]-=1
            if m[t[i]]==0:
                del m[t[i]]
        return True
