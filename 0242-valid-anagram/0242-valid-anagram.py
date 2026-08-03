class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m={}
        for chr in s:
            if chr not in m:
                m[chr]=1
            else:
                m[chr]+=1
        n={}
        for chr in t:
            if chr not in n:
                n[chr]=1
            else:
                n[chr]+=1
        if m==n:
            return True
        else:
            return False