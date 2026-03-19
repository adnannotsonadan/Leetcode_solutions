class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        st = []
        num = list(map(int, num))
        for i in range(n):
            while st and k and st[-1] > num[i] :
                st.pop()
                k -= 1
            if not k:
                st.extend(num[i:])
                break
            elif not st:
                st.append(num[i])
            else:
                if st[-1]<num[i] or st[-1]==num[i]:
                    st.append(num[i])
        if k:
            st = st[:-k]
        st="".join(map(str, st)).lstrip('0') or "0"
        return st