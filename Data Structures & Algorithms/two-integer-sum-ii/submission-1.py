class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(0, len(numbers) - 1):
            newTarget = target - numbers[i]
            print(numbers[i + 1 : ])
            if newTarget in numbers[i + 1 : ]:
                return [i + 1, numbers[i + 1: ].index(newTarget) + 1 + i + 1]
        