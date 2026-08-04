class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = set()

        def permutations(i, arr):
            if i >= len(nums):
                res.add(tuple(arr[::]))
                return
            
            for j in range(i, len(nums)):
                # if j > i and arr[j] == arr[j-1]:
                #     continue
                arr[j], arr[i] = arr[i], arr[j]
                permutations(i + 1, arr)
                arr[j], arr[i] = arr[i], arr[j]
        permutations(0, nums[::])
        return [list(tup) for tup in res]