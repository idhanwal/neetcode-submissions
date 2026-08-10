class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = []

        for num in stones:
            heapq.heappush(maxHeap, -num)
        

        while len(maxHeap) >= 2:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x == y:
                continue
            elif x < y or y < x:
                remaining = abs(x - y)
                heapq.heappush(maxHeap, -remaining)
        
        return -maxHeap[0] if maxHeap else 0

