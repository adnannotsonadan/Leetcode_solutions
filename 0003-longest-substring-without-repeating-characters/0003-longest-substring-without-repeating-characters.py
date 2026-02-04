class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # n = len(s)
        # res = 0
        # for i in range(n):
        #     seen = set()
        #     for j in range(i, n):
        #         if s[j] in seen:
        #             break
        #         else:
        #             seen.add(s[j])
        #             res = max(res, j - i + 1)
        # return res

        low=0
        high=0
        maxl=0
        t=''
        while high<len(s):
            if s[high] not in t:
                t+=s[high]
                if len(t)>maxl:
                    maxl=len(t)
                high+=1
            else:
                low=high
                t=''
        return maxl