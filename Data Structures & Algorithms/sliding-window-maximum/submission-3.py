class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxStack = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while maxStack and maxStack[-1] < nums[r]:
                maxStack.pop()
            maxStack.append(nums[r])

            if r >= k - 1:
                res.append(maxStack[0])
                if nums[l] == maxStack[0]:
                    maxStack.popleft()
                l += 1
                
        return res
                

