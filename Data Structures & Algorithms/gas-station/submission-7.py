class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        

        n = len(gas)
        # max_savings = float('-inf')
        start = 0
        launch_idx = []
        for i in range(n):
            if gas[i] - cost[i] >= 0:
                max_savings = gas[i] - cost[i]
                launch_idx.append(i)
        # if max_savings < 0:
        #     return -1
        print(launch_idx)
        for start in launch_idx:
            end = start + 1
            if end == n:
                end = 0
            tank = gas[start] - cost[start]
            while start != end:
                tank += gas[end] - cost[end]
                if tank < 0:
                    break
                end += 1
                if end == n:
                    end = 0
            if start == end:
                return start
        return -1
