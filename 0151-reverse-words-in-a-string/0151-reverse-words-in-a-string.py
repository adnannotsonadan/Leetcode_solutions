class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s=s.split()
        s.reverse()
        x=" ".join(s)
        # for ch in x:
        #     ch.replace(")
        return x