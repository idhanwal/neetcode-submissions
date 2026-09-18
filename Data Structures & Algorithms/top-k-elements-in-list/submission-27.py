class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]
        # print(count)
        freqCount = Counter(nums)
        # print(freqCount.items())
        for key, value in freqCount.items():
            count[value].append(key)
        res = []
        # print(count)
        for value in range(len(count) - 1, -1, -1):
            if count[value]:
                while count[value]:
                    res.append(count[value].pop())
                    if len(res) == k:
                        return res
        return []