class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]
        freqCount = Counter(nums)
        for key, value in freqCount.items():
            count[value].append(key)
        res = []
        for value in range(len(count) - 1, -1, -1):
            if count[value]:
                while count[value]:
                    res.append(count[value].pop())
                    if len(res) == k:
                        return res
        return []