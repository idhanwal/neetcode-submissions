class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = 0
        for r in range(len(numbers)):
            t = target - numbers[r]
            left = r
            right = len(numbers) - 1

            while left <= right:
                m = (right + left) // 2
                if numbers[m] == t:
                    return [r + 1, m + 1]
                elif numbers[m] < t:
                    left = m + 1
                elif numbers[m] > t:
                    right = m - 1
            




        