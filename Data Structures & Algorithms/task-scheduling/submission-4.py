class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        cooldown = deque()
        time = 0

        while maxHeap or cooldown:
            time += 1
            if not maxHeap:
                time = cooldown[0][1]
            else:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt != 0:
                    cooldown.append([cnt, time + n])
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])
            
        return time












