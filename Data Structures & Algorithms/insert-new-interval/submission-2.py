class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
        res = [intervals[0]]

        for start, end in intervals[1:]:
            print(res)
            if res[-1][1] > end:
                continue
            elif res[-1][1] >= start:
                res[-1][1] = end
            else:
                res.append([start, end])
        return res