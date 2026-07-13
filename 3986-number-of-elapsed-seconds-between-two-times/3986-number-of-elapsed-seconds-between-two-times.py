class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        count=0
        Shrs=''
        Smins=''
        Ssecs=''
        for i in range(2):
            Shrs+=startTime[i]
        for i in range(3,5):
            Smins+=startTime[i]
        for i in range(6,len(startTime)):
            Ssecs+=startTime[i]
        Shrs=int(Shrs)
        Smins=int(Smins)
        Ssecs=int(Ssecs)

        Ehrs=''
        Emins=''
        Esecs=''
        for i in range(2):
            Ehrs+=endTime[i]
        for i in range(3,5):
            Emins+=endTime[i]
        for i in range(6,len(endTime)):
            Esecs+=endTime[i]

        Ehrs=int(Ehrs)
        Emins=int(Emins)
        Esecs=int(Esecs)
        
        st=Shrs*3600+Smins*60+Ssecs
        end=Ehrs*3600+Emins*60+Esecs
        tot=end-st

        return tot
