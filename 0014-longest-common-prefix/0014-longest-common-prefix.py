class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        st=strs[0]
        end=strs[-1]
        s=''
        for i in range(len(st)):
            if st[i]==end[i]:
                s+=st[i]
            else:
                break
        return s