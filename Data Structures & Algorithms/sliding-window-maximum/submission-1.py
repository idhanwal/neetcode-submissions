class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        r = 0
        heap = []
        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            if r >= k - 1:
                while heap[0][1] <= r - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
            
