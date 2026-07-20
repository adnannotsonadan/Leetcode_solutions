class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        op=[intervals[0]]
        for i in range(1,len(intervals)):
            for j in range(2):
                if intervals[i][0]<=op[-1][1]:
                    op[-1][1]=max(op[-1][1],intervals[i][1])
                else:
                    op.append(intervals[i])
        return op
        