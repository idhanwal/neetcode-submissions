class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = currSum = 0

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        for num in nums:
            currSum += num

            diff = currSum - k

            res += prefix_sum[diff]
            prefix_sum[currSum] += 1
        
        return res