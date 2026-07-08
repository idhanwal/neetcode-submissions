class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums:
            if n in d:
                d[n] = d[n] + 1
            else:
                d[n] = 1
        
        sorted_dict = dict(sorted(d.items(), key=lambda item:item[1], reverse=True))
        print(sorted_dict)
        res = []
        for key in sorted_dict.items():
            if k > 0:
                res.append(key[0])
                k -= 1
        
        return res
