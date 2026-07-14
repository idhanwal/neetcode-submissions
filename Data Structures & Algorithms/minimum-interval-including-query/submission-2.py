class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort(key= lambda x: x[1] - x[0] + 1)
        
        res = []

        for q in queries:
            i = 0
            while i < len(intervals):
                if intervals[i][0] <= q <= intervals[i][1]:
                    res.append(intervals[i][1] - intervals[i][0] + 1)
                    break
                i += 1
            else:
                res.append(-1)
        
        return res