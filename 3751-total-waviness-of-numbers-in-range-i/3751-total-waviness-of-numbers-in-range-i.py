class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        count=0
        for i in range(num1,num2+1):
            st=str(i)
            for j in range(1,len(st)-1):
                if st[j]>st[j-1] and st[j]>st[j+1]:
                    count+=1
                if st[j]<st[j-1] and st[j]<st[j+1]:
                    count+=1
        return count