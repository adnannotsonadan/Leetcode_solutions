class Solution:
    def frequencySort(self, s: str) -> str:
        m={}
        for ch in s:
            if ch not in m:
                m[ch]=1
            else:
                m[ch]+=1
        x=sorted(m.items(),key=lambda x:x[1],reverse=True)
        ans=''

        for key,val in x:
            ans+=key*val
        return ans