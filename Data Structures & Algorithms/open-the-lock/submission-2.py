class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # deadends = set(deadends)
        # if target == "0000":
        #     return 0
        visit = set(deadends)

        if "0000" in visit:
            return -1
        
        queue = deque(["0000"])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                lock = queue.popleft()
                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        newLock = lock[0 : i] + digit + lock[i + 1: ]
                        if newLock not in visit:
                            if newLock == target:
                                return steps
                            queue.append(newLock)
                            visit.add(newLock)
        return -1
