class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = Counter(nums)
        heap = []

        for key in mapper:
            heapq.heappush(heap, (-mapper[key], key))
        
        res = []
        while k > 0:
            value, key = heapq.heappop(heap)
            k -= 1
            res.append(key)
        
        return res
        

