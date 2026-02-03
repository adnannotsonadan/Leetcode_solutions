class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        lsum=0
        rsum=0
        msum=0
        for i in range(k):
            lsum+=cardPoints[i]
            msum=lsum
        rind=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rind]
            rind-=1
            msum=max(msum,lsum+rsum)
        return msum