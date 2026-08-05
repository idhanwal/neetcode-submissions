class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # deadends = set(deadends)
        if "0000" in deadends:
            return -1

        def children(code):
            variations = []
            for i in range(4):
                digit = str((int(code[i]) + 1) % 10)
                variations.append(code[0: i] + digit + code[i + 1:])
                digit = str((int(code[i]) - 1 + 10) % 10)
                variations.append(code[0: i] + digit + code[i + 1: ])
            return variations
            

        queue = deque([("0000", 0)])
        visit = set(deadends)
        

        while queue:
            code, turns = queue.popleft()
            if code == target:
                return turns
            
            for child in children(code):
                if child not in visit:
                    visit.add(child)
                    queue.append((child, turns + 1))
        return -1