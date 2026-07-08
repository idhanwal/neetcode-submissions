class MedianFinder:

    def __init__(self):
        self.minH, self.maxH = [], [] # minH will have large elements and maxH will have smaller elements
        

    def addNum(self, num: int) -> None:
        if self.minH and self.minH[0] < num:
            heapq.heappush(self.minH, num)
        else:
            heapq.heappush(self.maxH, -1 * num)
        
        if len(self.minH) > len(self.maxH) + 1:
            val = heapq.heappop(self.minH)
            heapq.heappush(self.maxH, -1 * val)
        if len(self.maxH) > len(self.minH) + 1:
            val = -1 * heapq.heappop(self.maxH)
            heapq.heappush(self.minH, val)
        

    def findMedian(self) -> float:
        if len(self.minH) > len(self.maxH):
            return self.minH[0]
        elif len(self.minH) < len(self.maxH):
            return -1 * self.maxH[0]
        return (self.minH[0] + (-1 * self.maxH[0])) / 2.0
        
        