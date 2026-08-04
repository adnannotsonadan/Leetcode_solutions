class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        
        newS=s.split(' ')
        print(newS)
        y=[]
        for char in newS:
            if char.isalnum():
                y.append(char)
        y.reverse()
        x=" ".join(y)
        return x
        