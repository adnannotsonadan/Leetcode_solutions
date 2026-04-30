class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # t="".join(sorted(t))
        # s="".join(sorted(s))
        # if s==t:
        #     return True
        # else:
        #     return False
                
        ms={}
        mt={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in ms:
                ms[s[i]]=1
            else:
                ms[s[i]]+=1
            if t[i] not in mt:
                mt[t[i]]=1
            else:
                mt[t[i]]+=1
        if ms==mt:
            return True
        return False