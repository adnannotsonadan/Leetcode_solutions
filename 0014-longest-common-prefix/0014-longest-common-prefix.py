class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # s=""
        # strs.sort()
        # if not strs:
        #     return s
        # first=strs[0]
        # last=strs[-1]
        # for i in range(len(first)):
        #     if first[i]==last[i]:
        #         s+=first[i]
        #     else:
        #         break
        # return s

        s=''
        if not strs:
            return s
        strs.sort()
        f=strs[0]
        l=strs[-1]

        for i in range(len(f)):
            if f[i]==l[i]:
                s+=f[i]
            else:
                break
        return s
